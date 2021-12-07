from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe
from django.conf import settings
from users.tasks import send_user_email
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from users.models import User
from django.db.models import F,Q
from users.models import Invoice
from rest_framework import viewsets
from .serializers import (
    ProductSerializer
)
from django.db.models.functions import Now
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError


stripe.api_key = settings.STRIPE_SEC_KEY

@api_view(['GET'])
def setup_intent(request):
    data = stripe.SetupIntent.create(
        payment_method_types=['card'],
        customer=request.user.stripe_cust_id
    )
    return Response(data)


@api_view(['POST'])
def remove_paymentmethod(request):
    user = request.user
    try:
        if request.POST.get('payMethodId') == user.payment_method_id:
            stripe.PaymentMethod.detach(user.payment_method_id)
            user.payment_method_id = None
            send_user_email.delay(user.pk, 'card_removed',
                                  last_4=user.stripe_last4)
            user.stripe_last4 = None
            user.card_brand = None
            user.save()
            return Response({
                'status': True
            })
    except Exception as e:
        pass
    return Response({
        'status': False
    }, status=400)


@require_http_methods(['POST'])
def stripe_webhooks(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
        data = event.data.object
        amount = None
        credits = 0
        user_obj = User.objects.filter(stripe_cust_id=data.customer).first()
        user_curr_price = user_obj.curr_price
        if event.type == 'charge.succeeded':
            if data.amount_captured > 0 and data.amount == data.amount_captured:
                amount = float(data.amount_captured/100)

                credits = int((1000/user_curr_price)*amount)

        if event.type == 'charge.refunded':
            if data.amount_refunded > 0:
                amount = -float(data.amount_refunded/100)
                credits = int((1000/user_curr_price)*amount)
                
        if event.type in ['invoice.payment_action_required', 'invoice.payment_failed']:
            send_user_email.delay(user_obj.pk, 'payment_failed')

        if str(event.type).startswith('invoice.'):
            invoice_obj, created = Invoice.objects.get_or_create(
                user=user_obj,
                stripe_id=data.id)
            invoice_obj.status = data.status
            invoice_obj.url = data.hosted_invoice_url
            invoice_obj.cost = float(data.amount_due/100)
            invoice_obj.save()

        if amount is not None:
            if user_obj:
                User.objects.filter(pk=user_obj.pk).update(
                    credit=F('credit')+credits)
                if amount > 0:
                    send_user_email.delay(
                        user_obj.pk, 'payment_succeeded', amount=str(amount))
                    
                    # Notify admins
                    admins = User.objects.filter(is_superuser=True).all()
                    for admin in admins:
                        customer_name = f'{user_obj.first_name} {user_obj.last_name}'
                        send_user_email.delay(admin.pk, 'payment_admins_notify', customer=customer_name, amount=str(amount))
                elif amount < 0:
                    send_user_email.delay(
                        user_obj.pk, 'payment_refunded', amount=str(amount).replace('-', ''))

        return JsonResponse({
            'status': True
        }, status=200)
    except Exception as e:
        return JsonResponse({
            'status': str(e)
        }, status=400)


@api_view(['POST'])
def save_payment_method(request):
    user = request.user
    paymethodId = request.POST.get('payMethodId')
    error_msg = 'An uknown error occured.'

    try:
        pm = stripe.PaymentMethod.retrieve(paymethodId)
        if not user.stripe_cust_id:
            user.setup_stripe_customer()

        if pm:
            stripe.Customer.modify(user.stripe_cust_id,
                                   invoice_settings={
                                       'default_payment_method': paymethodId}
                                   )
            if user.payment_method_id and user.payment_method_id != paymethodId:
                try:
                    stripe.PaymentMethod.detach(user.payment_method_id)
                except Exception as e:
                    pass
            user.payment_method_id = paymethodId
            user.stripe_last4 = pm.card.last4
            user.card_brand = pm.card.brand
            user.save()
            # send_user_email.delay(user.pk, 'card_added',
            #                       last_4=user.stripe_last4)
            return Response({
                'message': 'Payment method has been added successfully.'
            })
    except Exception as e:
        error_msg = str(e)

    return Response({
        'error': error_msg
    }, status=400)



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('pk')
    serializer_class = ProductSerializer

    def filter_queryset(self, queryset):
        if self.request.GET.get('status'):
            queryset = queryset.filter(product_status=True)

        order_by = self.request.GET.get('order_by')
        if order_by:
            if order_by.lstrip('-') in ['product_name', 'created_at', 'updated_at']:
                queryset = queryset.order_by(order_by)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(product_name__icontains=search) | Q(
                product_description__icontains=search))

        return queryset

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        try:
            stripe.Price.modify(product.product_stripe_price_id,active=False)
            stripe.Product.modify(product.product_stripe_id,active=False)
        except:
            raise ValidationError('Error')
        product.delete()
        return Response(data='Successfully deleted!')


@api_view(['POST'])
def subscribe(request):
    product_id = int(request.POST.get('product_id'))
    
    if request.user.stripe_cust_id is not None and request.user.payment_method_id is not None:
        product = Product.objects.filter(pk=product_id).first()
        if product is not None:
            try:
                subs = stripe.Subscription.create(
                    customer=request.user.stripe_cust_id,
                    items=[
                        {"price": product.product_stripe_price_id},
                    ],
                )
                request.user.stripe_sub_id = subs.id
                request.user.save()
                request.user.subscriptions.add(product)
                return JsonResponse({'message':'Subscribed Successfully!', 'status':True}, status=200)
            except:
                return JsonResponse({'message':'Error while subscribing!', 'status':False},status=403)
        else:
            raise JsonResponse({'message':'Product Not Avaliable!', 'status':False},status=403)
    else:
        raise JsonResponse({'message':'Payment Method not attached!', 'status':False},status=403)

@api_view(['POST'])
def unsubscribe(request):
    product_id = int(request.POST.get('product_id'))
    
    user = request.user
    
    if request.user.stripe_sub_id is not None:
        try:
            stripe.Subscription.modify(
                request.user.stripe_sub_id,
                cancel_at_period_end=True
            )
            user.subscriptions.remove(product_id)
            return JsonResponse({'message':'Unsubscribed Successfully!', 'status':True}, status=200)
        except Exception as e:
            return JsonResponse({'message':str(e), 'status':False}, status=403)
    return JsonResponse({'message':'Subscription is not found!', 'status':False},status=403)
        

@api_view(['GET'])
def get_subscribe(request):
    user = request.user
    subs = user.subscriptions.first()
    if subs is not None:
        return Response({'product_id': subs.pk})
    else:
        return Response({'product_id':''})

@api_view(['POST'])
def switch_subscription(request):
    product_id = int(request.POST.get('product_id'))
    if request.user.stripe_cust_id is not None and request.user.payment_method_id is not None:
        product = Product.objects.filter(pk=product_id).first()
        
        if product is not None:
            user =request.user
            subs = user.subscriptions.first()
            if subs:
                user.subscriptions.remove(subs.pk)
                stripe.Subscription.modify(
                    user.stripe_sub_id,
                    cancel_at_period_end=True
                )
            try:
                subs = stripe.Subscription.create(
                    customer=request.user.stripe_cust_id,
                    items=[
                        {"price": product.product_stripe_price_id},
                    ],
                )
                request.user.stripe_sub_id = subs.id
                request.user.save()
                request.user.subscriptions.add(product)
                return JsonResponse({'message':'Subscribed Successfully!', 'status':True}, status=200)
            except:
                return JsonResponse({'message':'Error while subscribing!', 'status':False},status=403)
        else:
            raise JsonResponse({'message':'Product Not Avaliable!', 'status':False},status=403)
    else:
        raise JsonResponse({'message':'Payment Method not attached!', 'status':False},status=403)
    