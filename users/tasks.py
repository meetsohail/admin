from celery import shared_task
from .models import User, Email
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
import stripe


@shared_task
def send_user_email(user_id, email_type, **kwargs):
    user = User.objects.filter(pk=user_id).first()
    em = Email.objects.filter(email_type=email_type, is_active=True).first()
    if user and em:
        kwargs['user'] = user
        kwargs['SITE_NAME'] = settings.SITE_NAME
        kwargs['SITE_URL'] = settings.SITE_URL
        kwargs['EMAIL_PARAGRAPH_CLASS'] = 'font-family: sans-serif; font-size: 16px; font-weight: normal; margin: 0; Margin-bottom: 16px;'
        kwargs['show_footer'] = em.show_footer
        html_message = em.get_email_content(content_type='html', **kwargs)
        text_message = em.get_email_content(content_type='text', **kwargs)
        subject = em.get_email_subject(**kwargs)
        from_email = settings.FROM_EMAIL
        try:
            send_mail(subject, text_message, from_email, [user.email], html_message=html_message)
            return True
        except BadHeaderError:
            pass
        return False

@shared_task
def charge_customer(user_id, quantity, billing_method='charge_default_method'):
    user = User.objects.filter(id=user_id).first()
    if user and user.stripe_cust_id:
        stripe.api_key = settings.STRIPE_SEC_KEY
        stripe.InvoiceItem.create(
            customer=user.stripe_cust_id,
            price=settings.STRIPE_PRICE_ID,
            quantity=quantity
        )
        if billing_method == 'charge_default_method':
            inv = stripe.Invoice.create(
                customer=user.stripe_cust_id,
                collection_method='charge_automatically', statement_descriptor=settings.SITE_NAME)
            stripe.Invoice.pay(inv.id)
        elif billing_method == 'send_email':
            inv = stripe.Invoice.create(
                customer=user.stripe_cust_id,
                collection_method='send_invoice', statement_descriptor=settings.SITE_NAME, days_until_due=7)
            stripe.Invoice.send_invoice(inv.id)


@shared_task
def setup_initial_user(user_id):
    user = User.objects.filter(pk=user_id).first()
    if user:
        user.reset_stats()

        if settings.SEND_WELCOME_EMAIL is True:
            send_user_email.delay(user.pk, email_type='welcome')

        if settings.SETUP_STRIPE_CUSTOMER is True:
            user.setup_stripe_customer()
        return True
    return False