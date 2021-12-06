from django.http import JsonResponse
from users.models import User, Location
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from users.serializers import UserSerializer
import validators
from users import tasks
from django.db.models import F

def get_ip_loc(request, record_type='login'):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    if validators.ipv4(ip):
        loc_obj, created = Location.objects.get_or_create(ip_address=ip, record_type=record_type)
        return loc_obj
    return False

def login_view(request):
    loc_obj = get_ip_loc(request)
    if request.method == 'POST':
        if loc_obj:
            mutable = request.POST._mutable
            request.POST._mutable = True
            request.POST['ip_address'] = loc_obj.ip_address
            request.POST._mutable = mutable
        f = LoginForm(data=request.POST)
        errors = {}
        if f.is_valid():
            email = f.cleaned_data.get('email')
            password = f.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if loc_obj:
                    loc_obj.failed_logins = 0
                    loc_obj.save()
                    if not loc_obj in user.locations.all():
                        # tasks.send_user_email.delay(user.pk, 'loginalert', new_ip=loc_obj.ip_address)
                        user.locations.add(loc_obj)
                return JsonResponse({
                    'status': True,
                    'user': UserSerializer(instance=request.user).data
                })
            else:
                formerrors = {
                    'email': ['The provided login info is invalid.']
                }
        else:
            formerrors = dict(f.errors)
    
    if loc_obj:
        Location.objects.filter(pk=loc_obj.pk).update(failed_logins=F('failed_logins')+1)

    return JsonResponse({
        'status': False,
        'errors': formerrors
    }, status=422)

def register_view(request):
    logout(request)
    if request.method == 'POST':
        loc_obj = get_ip_loc(request, 'register')
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['ip_address'] = loc_obj.ip_address
        request.POST._mutable = mutable
        f = RegisterForm(data=request.POST)
        errors = {}
        if f.is_valid():
            user = User.objects.create(
                first_name=f.cleaned_data.get('first_name'),
                last_name=f.cleaned_data.get('last_name'),
                email=f.cleaned_data.get('email'),
                password=make_password(f.cleaned_data.get('password'))
            )
            login(request, user)
            if loc_obj:
                user.locations.add(loc_obj)
            return JsonResponse({
                'status': True,
                'user': UserSerializer(instance=user).data
            })
        else:
            return JsonResponse({
                'errors': dict(f.errors)
            }, status=422)
    return JsonResponse({
        'status': False
    }, status=400)

def reset_view(request):
    if request.method == 'POST':
        try:
            f = PasswordResetForm(data=request.POST)
            assert f.is_valid()
            f.save(request=request)
            return JsonResponse({
                'status': True
            })
        except:
            pass
    return JsonResponse({
        'status': False
    }, status=400)

def update_pass_view(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST.get('email')).first()
        if user:
            f = SetPasswordForm(user=user, data=request.POST)
            tok = request.POST.get('token')
            pg = PasswordResetTokenGenerator()
            if f.is_valid():
                del user.password
                if pg.check_token(user, tok):
                    f.save()
                    login(request, user)
                    return JsonResponse({
                        'status': True,
                        'user': UserSerializer(instance=user).data
                    })
            else:
                return JsonResponse({
                    'errors': dict(f.errors)
                }, status=400)
    return JsonResponse({
        'errors': {
            'new_password1': ['The password reset token is either invalid or expired.']
        }
    }, status=400)
