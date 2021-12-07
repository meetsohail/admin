from django.test import TestCase
from users.tasks import send_user_email
from users.models import User
from django.core.management import call_command


class TestEmails(TestCase):

    def setUp(self):
        call_command('seedemails')

    def test_welcome_email(self):
        send_user_email(1, email_type='welcome')
    
    def test_job_created_email(self):
        send_user_email.delay(1, email_type='jobqueued', job_id=123, job_title='Test Job')
    
    def test_job_completed_email(self):
        send_user_email.delay(1, email_type='jobcompleted', job_id=123, job_title='Test Job')

    def test_card_removed_email(self):
        send_user_email.delay(1, email_type='card_removed', last_4=2332)
    
    def test_card_added_email(self):
        send_user_email.delay(1, email_type='card_added', last_4=2332)
    
    def test_login_alert_email(self):
        send_user_email.delay(1, email_type='loginalert', new_ip='37.111.128.43')