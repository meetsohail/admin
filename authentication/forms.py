from django import forms
from users.models import User, Location
from django.core import exceptions
from django.contrib.auth import password_validation
from django.conf import settings


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    ip_address = forms.CharField(required=False)

    def clean(self):
        ip_address = self.cleaned_data.get('ip_address')
        if ip_address:
            loc_obj = Location.objects.filter(ip_address=ip_address, record_type='login').first()
            if loc_obj and loc_obj.failed_logins > settings.MAX_FAILED_LOGINS:
                self.add_error('email', f'The IP {ip_address} has been blacklisted.')

class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    ip_address = forms.CharField(required=False)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if all([password, confirm_password, (password != confirm_password)]):
            self.add_error('password', 'Password and the confirm password do not match.')
        
        ip_address = self.cleaned_data.get('ip_address')
        if ip_address:
            loc_obj = Location.objects.filter(ip_address=ip_address, record_type='register').first()
            if loc_obj and loc_obj.users.count() >= settings.MAX_USERS_PER_IP:
                self.add_error('email', f'The IP {ip_address} has been used too many times.')
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            password_validation.validate_password(password=password)
        except exceptions.ValidationError as e:
            for err in list(e.messages):
                self.add_error('password', err)
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email address is already in use.')
        return email