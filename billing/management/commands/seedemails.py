from django.core.management.base import BaseCommand
from users.models import Email
from django.conf import settings


class Command(BaseCommand):
    help = 'Seed email templates.'

    def handle(self, *args, **options):
        emails = [
            {
                'email_type': 'welcome',
                'email_subject': 'Welcome to {{ SITE_NAME }}',
                'email_content': 'Hi {{ user.first_name }},<br><br>Welcome to {{ SITE_NAME }}. We are pleased to have you onboard and we hope you will like our service.<br><br>If you have any question, don\'t hesitate to contact our support team (support@rankspy.net).'
            },
            {
                'email_type': 'jobcompleted',
                'email_subject': '{{ SITE_NAME }} bulk job #{{ job_id }} completed',
                'email_content': 'Hi {{ user.first_name }},<br><br>Your bulk job at {{ SITE_NAME }} with ID #{{ job_id }} and title {{ job_title }} has completed. You can download the data file by signing into your {{ SITE_NAME }} account.<br><br>You should download your data for this job within 30 days. After 30 days our system automatically deletes old jobs and their associated data.'
            },
            {
                'email_type': 'card_removed',
                'email_subject': '{{ SITE_NAME }} credit card removed',
                'email_content': 'Hi {{ user.first_name }},<br><br>A credit or a debit card ending in <strong>****{{ last_4 }}</strong> has been removed from your {{ SITE_NAME }} billing account. To ensure that subscriptions don\'t fail, consider adding a new payment method.'
            },
            {
                'email_type': 'card_added',
                'email_subject': '{{ SITE_NAME }} credit card updated',
                'email_content': 'Hi {{ user.first_name }},<br><br>This email confirms that a credit or a debit card ending in <strong>****{{ last_4 }}</strong> has been added to your {{ SITE_NAME }} billing account.'
            },
            {
                'email_type': 'loginalert',
                'email_subject': '{{ SITE_NAME }} account sign in alert',
                'email_content': 'Hi {{ user.first_name }},<br><br>Someone has just signed in to your {{ SITE_NAME }} account from a location ({{ new_ip }}) that\'s unfamiliar to us.<br><br>If this seems to be suspicious, we highly recommend resetting your account password as soon as possible.'
            },
            {
                'email_type': 'lowbalance',
                'email_subject': '{{ SITE_NAME }} account balance exhausted',
                'email_content': 'Hi {{ user.first_name }},<br><br>Your {{ SITE_NAME }} account balance has exhausted and further jobs will fail unless you top-up your account again. You can recharge your account by signing into your {{ SITE_NAME }} account anytime.<br><br>Need help? Contact our support at support@rankspy.net.'
            },
            {
                'email_type': 'payment_succeeded',
                'email_subject': '{{ SITE_NAME }} account balance updated',
                'email_content': 'Hi {{ user.first_name }},<br><br>We confirm that a payment of ${{ amount }} USD was successfully applied to your {{ SITE_NAME }} financial account.'
            },
            {
                'email_type': 'free_trial',
                'email_subject': '{{ SITE_NAME }} free trial activated',
                'email_content': 'Hi {{ user.first_name }},<br><br>We confirm that ${{ amount }} USD of free credit was added to your {{ SITE_NAME }} balance.'
            },
            {
                'email_type': 'new_signup',
                'email_subject': '{{ SITE_NAME }} new sign-up',
                'email_content': 'Hi {{ user.first_name }},<br><br>Good news! A new user [{{ user_data }}] has just signed up at {{ SITE_NAME }}.'
            },
            {
                'email_type': 'payment_admins_notify',
                'email_subject': '{{ SITE_NAME }} new purchase',
                'email_content': 'Hi {{ user.first_name }},<br><br>Congrats! {{ customer }} has just topped-up their {{ SITE_NAME }} account with ${{ amount }} USD.'
            },
            {
                'email_type': 'payment_refunded',
                'email_subject': '{{ SITE_NAME }} payment refunded',
                'email_content': 'Hi {{ user.first_name }},<br><br>We confirm that a refund amounting ${{ amount }} USD was initiated by {{ SITE_NAME }} financial staff. You should see the money in your bank within a couple of days.'
            },
            {
                'email_type': 'payment_failed',
                'email_subject': '{{ SITE_NAME }} payment failed',
                'email_content': 'Hi {{ user.first_name }},<br><br>A payment attempt against one of your {{ SITE_NAME }} invoices has failed. Please contact support if the issue persists.'
            },
            {
                'email_type': 'apiaccessenabled',
                'email_subject': '{{ SITE_NAME }} API access enabled',
                'email_content': 'Hi {{ user.first_name }},<br><br>Your account is now in an eligible state to consume our API services. If you need any help, contact our support (support@rankspy.net).'
            },
            {
                'email_type': 'apiaccessdisabled',
                'email_subject': '{{ SITE_NAME }} API access disabled',
                'email_content': 'Hi {{ user.first_name }},<br><br>Your API access has been temporarily suspended. This is probably due to a lack of funds. If you need help please contact our support team (support@rankspy.net).'
            },
            {
                'email_type': 'ratelimitingchanged',
                'email_subject': '{{ SITE_NAME }} rate limit value changed',
                'email_content': 'Hi {{ user.first_name }},<br><br>Your API rate limit value has changed. New API requests limit is {{ new_value }} per second. If you have any questions please contact our support team (support@rankspy.net).'
            }
        ]
        for em in emails:
            Email.objects.filter(email_type=em.get('email_type')).delete()
            Email.objects.create(
                email_type=em.get('email_type'),
                email_subject=em.get('email_subject'),
                email_content=em.get('email_content'),
            )
