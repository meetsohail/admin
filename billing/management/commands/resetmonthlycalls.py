from django.core.management.base import BaseCommand
from users.models import User
from django.utils.timezone import make_aware
from datetime import datetime

class Command(BaseCommand):
    help = 'Reset monthly API calls volume.'

    def handle(self, *args, **options):
        i = 0
        for u in User.objects.filter(stats_reset_on__isnull=True).all():
            u.reset_stats()
            i += 1
        self.stdout.write(self.style.SUCCESS(f'{i} users last reset was set to null.'))

        users = User.objects.filter(stats_reset_on__lte=make_aware(datetime.now())).all()
        i = 0
        for u in users:
            u.reset_stats()
            i += 1
        self.stdout.write(self.style.SUCCESS(f'{i} users monthly calls have been reset.'))