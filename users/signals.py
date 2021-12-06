from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from users.tasks import setup_initial_user
from users.models import User
import django.dispatch
from users.tasks import send_user_email


def notify_low_balance(sender, **kwargs):
    send_user_email.delay(sender.pk, 'lowbalance')

low_balance = django.dispatch.Signal()
low_balance.connect(notify_low_balance)

@receiver(post_save, sender=User)
def setup_new_user(sender, instance=None, created=False, **kwargs):
    if created:
        # Notify admins
        admins = User.objects.filter(is_superuser=True).all()
        for admin in admins:
            user_data = f'{instance.first_name} {instance.last_name} ({instance.email})'
            send_user_email.delay(admin.pk, 'new_signup', user_data=user_data)
        setup_initial_user.delay(instance.pk)

@receiver(pre_delete, sender=User)
def delete_user_obj(sender, instance=None, **kwargs):
    if instance:
        instance.clean_user_data()