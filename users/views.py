import json
from django.http.response import JsonResponse
from rest_framework import viewsets
from .serializers import (
    UserSerializer, LogSerializer, InvoiceSerializer, UserSettingUpdateSerializer
)
from .models import Invoice, User, Log
from rest_framework.permissions import IsAdminUser
from .permissions import IsSameUserOrAdmin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from django.views.decorators.http import require_http_methods
from django.db.models import Q, F
import datetime
from django.utils import timezone as tz
from .tasks import send_user_email


@api_view()
@permission_classes([IsAuthenticated])
def authenticated_user(request):
    return Response(UserSerializer(instance=request.user).data)


@api_view()
@permission_classes([IsAuthenticated])
def get_api_key(request):
    return Response({
        'api_key': request.user.apitoken
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reset_api_key(request):
    Token.objects.filter(user=request.user).delete()
    token = Token.objects.create(user=request.user)
    return Response({
        'api_key': token.key
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsSameUserOrAdmin]
        return [permission() for permission in permission_classes]

    def filter_queryset(self, queryset):
        order_by = self.request.GET.get('order_by')
        if order_by:
            if order_by.lstrip('-') in ['balance', 'monthly_calls', 'alltime_calls', 'date_joined']:
                queryset = queryset.order_by(order_by)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(email__icontains=search) | Q(
                first_name__icontains=search) | Q(last_name__icontains=search))

        return queryset


class LogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Log.objects.all().order_by('-pk')
    serializer_class = LogSerializer

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        order_by = self.request.GET.get('order_by')
        if order_by:
            if order_by.lstrip('-') in ['pk', 'url', 'status', 'created_at']:
                queryset = queryset.order_by(order_by)

        status = self.request.GET.get('status')
        if status and status in ['successful', 'failed']:
            if status == 'successful':
                queryset = queryset.filter(status=200)
            else:
                queryset = queryset.exclude(status=200)

        return queryset


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.all().order_by('-pk')
    serializer_class = InvoiceSerializer

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        order_by = self.request.GET.get('order_by')
        if order_by:
            if order_by.lstrip('-') in ['pk', 'cost', 'status', 'date']:
                queryset = queryset.order_by(order_by)

        status = self.request.GET.get('status')
        if status and status in ['paid', 'open', 'draft', 'uncollectible', 'void']:
            queryset = queryset.filter(status=status)

        return queryset


@api_view(['GET'])
def analytics_summary(request):
    user = request.user

    total = Log.objects.filter(user=user).count()
    success_count = Log.objects.filter(user=user, status=200).count()
    failed_count = Log.objects.filter(user=user).exclude(status=200).count()
    successful = 0
    failed = 0
    if total > 0:
        successful = min((success_count/total*100), 100)
        failed = min((failed_count/total*100), 100)
    d = tz.now() - datetime.timedelta(seconds=2)
    data = {
        'req_count': Log.objects.filter(user=user, created_at__gt=d).count(),
        'breakdown': {
            'successful': successful,
            'failed': failed
        }
    }

    return Response({
        'data': data
    })


@require_http_methods(['POST'])
def update_settings(request, id):
    if request.user.is_superuser:
        settings_serializer = UserSettingUpdateSerializer(data=request.POST)
        if settings_serializer.is_valid():
            data = settings_serializer.validated_data
            user = User.objects.filter(pk=id).first()

            # Update custom prices
            user.cust_price = data.get('cust_price')
            user.save()

            # Update balance
            if data.get('credit') is not None:
                amount = data.get('credit')
                if amount != 0:
                    User.objects.filter(id=user.id).update(
                        credit=F('credit')+amount)
                    
            return JsonResponse({
                'status': True
            })
        else:
            return JsonResponse({
                'errors': dict(settings_serializer.errors)
            }, status=422)

    return JsonResponse({
        'detail': 'You are not allowed!'
    }, status=401)
