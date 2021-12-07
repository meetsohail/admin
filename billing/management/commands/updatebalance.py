from django.core.management.base import BaseCommand
from users.models import User
from django.db.models import F


class Command(BaseCommand):
    help = 'Update balance of users.'

    def add_arguments(self, parser):
        parser.add_argument('emails', nargs='+', type=str)
        parser.add_argument('balance', type=int)

    def handle(self, *args, **options):
        for email in options['emails']:
            user = User.objects.filter(email=email).first()
            if user:
                User.objects.filter(pk=user.pk).update(balance=F('balance')+options['balance'])
                self.stdout.write(self.style.SUCCESS(f'Balance has been updated for {user.email}'))

        