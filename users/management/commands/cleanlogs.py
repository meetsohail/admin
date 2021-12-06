from django.core.management.base import BaseCommand
from users.models import User, Log


class Command(BaseCommand):
    help = 'Delete old analytics data.'

    def handle(self, *args, **options):
        for user in User.objects.all():
            if user.logs.count() > 1000:
                self.stdout.write(self.style.SUCCESS(f'Deleting logs for {user}'))
                ids = Log.objects.filter(user=user).order_by('-pk').values_list('id', flat=True)[:1000]
                Log.objects.exclude(pk__in=ids).delete()