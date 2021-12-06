from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
import stripe
from rest_framework.authtoken.models import Token
from django.template.loader import render_to_string
from django.template import Template, Context
from django.utils.html import strip_tags
from django.utils.timezone import make_aware
from datetime import datetime
from dateutil.relativedelta import relativedelta



class CustomUserManager(BaseUserManager):
    '''
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is 'UserManager'
    '''
    def _create_user(self, email, password, **extra_fields):
        '''
        Creates and saves a User with the given email and password.
        '''
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class Location(models.Model):
    ip_address = models.CharField(max_length=255)
    ip_location = models.CharField(max_length=255, null=True, blank=True)
    record_type = models.CharField(max_length=50, default='login')
    failed_logins = models.IntegerField(default=0)
    is_blacklisted = models.BooleanField(default=False)
    blacklisted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True)
    trial_used = models.BooleanField(default=False)
    stripe_cust_id = models.CharField(max_length=255, null=True)
    stripe_sub_id = models.CharField(max_length=255, null=True)
    payment_method_id = models.CharField(max_length=150, null=True)
    stripe_last4 = models.CharField(max_length=10, null=True)
    card_brand = models.CharField(max_length=50, null=True)
    realtime_checks = models.IntegerField(default=0)
    stats_reset_on = models.DateTimeField(auto_now_add=True, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    @property
    def subscription(self):
        return self.subscriptions.first()

    def reset_stats(self):
        self.stats_reset_on = make_aware(datetime.now()+relativedelta(months=+1))
        self.monthly_calls = 0
        self.save()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
    
    
    @property
    def apikeys(self):
        return Token.objects.filter(user=self.pk).count()
    
    @property
    def apitoken(self):
        api_tok = Token.objects.filter(user=self.pk).first()
        if api_tok:
            return api_tok.key
        return None
    
    @property
    def curr_price(self):
        price = float(settings.BASE_PRICE_PER_1000)
        user_subscribe = self.subscriptions.first()
        if user_subscribe:
            if user_subscribe.credit_rate:
                return user_subscribe.credit_rate
        return price
        
          
    @property
    def avatar_url(self):
        import hashlib
        from urllib.parse import urlencode
        size = 60
        return f"https://www.gravatar.com/avatar/{hashlib.md5(self.email.encode('utf-8')).hexdigest()}?{urlencode({'s': str(size)})}"

    def setup_stripe_customer(self):
        stripe.api_key = settings.STRIPE_SEC_KEY
        has_stripe = False
        if self.stripe_cust_id:
            try:
                cust = stripe.Customer.retrieve(self.stripe_cust_id)
                if cust:
                    has_stripe = True
            except stripe.error.InvalidRequestError:
                pass
        

        if not has_stripe:
            try:
                cust_name = f'{self.first_name} {self.last_name}'
                customer = stripe.Customer.create(
                    name=cust_name,
                    email=self.email, 
                    metadata={'pk': self.pk}
                )
                self.stripe_cust_id = customer.id
                self.save()
            except stripe.error.InvalidRequestError:
                return False
        return True
    
    def clean_user_data(self):
        if self.stripe_cust_id:
            stripe.api_key = settings.STRIPE_SEC_KEY
            try:
                stripe.Customer.delete(self.stripe_cust_id)
            except:
                pass


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')
    stripe_id = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=500, null=True, default='javascript:void(0)')
    status = models.CharField(max_length=50, default='open')
    cost = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True)

EMAIL_TYPE_CHOICES = (
    ('welcome', 'Welcome',),
    ('card_removed', 'Card Removed',),
    ('card_added', 'Card Added',),
    ('loginalert', 'Login Alert',),
    ('jobqueued', 'Job Queued',),
    ('jobcompleted', 'Job Completed',),
    ('quotareached', 'Monthly Quota Reached',)
)

class Email(models.Model):
    email_type = models.CharField(max_length=255, unique=True, choices=EMAIL_TYPE_CHOICES)
    email_subject = models.CharField(max_length=255, default=f'Hello from {settings.SITE_NAME}')
    email_content = models.TextField()
    show_footer = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'[{self.email_type}] {self.email_subject}'
    
    def get_email_content(self, content_type='text', **kwargs):
        if content_type == 'text':
            the_content = strip_tags(self.email_content)
        else:
            the_content = self.email_content

        paragraphs = the_content.splitlines()
        kwargs['paragraphs'] = paragraphs
        if content_type == 'text':
            email_content = str(Template(render_to_string('users/emails/default.text', kwargs)).render(Context(kwargs)))
        else:
            email_content = str(Template(render_to_string('users/emails/default.html', kwargs)).render(Context(kwargs)))
        return email_content.strip()
    
    def get_email_subject(self, **kwargs):
        kwargs['email_subject'] = self.email_subject
        return Template(render_to_string('users/emails/subject.text', kwargs)).render(Context(kwargs)).strip()

class Log(models.Model):
    user = models.ForeignKey(User, related_name='logs', on_delete=models.CASCADE)
    url = models.CharField(max_length=500)
    method = models.CharField(max_length=20, default='POST')
    details = models.TextField(null=True, blank=True) 
    status = models.IntegerField(default=200)
    created_at = models.DateTimeField(auto_now_add=True)



