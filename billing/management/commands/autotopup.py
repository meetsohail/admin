from django.core.management.base import BaseCommand
from users.models import User
from django.db.models import F, Q
from users.tasks import charge_customer


class Command(BaseCommand):
    help = 'Process auto top-ups.'

    def handle(self, *args, **options):
        users = User.objects.filter(
            auto_topup=True, auto_topup_amount__gt=0, balance__lt=F('auto_topup_threshold')).all()
        for user in users:
            if user.stripe_cust_id and user.invoices.filter(Q(status='draft') | Q(status='open')).count() == 0:
                self.stdout.write(self.style.SUCCESS(
                    f'Processing auto top-up {user.auto_topup_amount} USD for {user}'))
                quantity = int(user.auto_topup_amount)
                charge_customer.delay(
                    user.pk, quantity=quantity, billing_method=user.auto_topup_method)
