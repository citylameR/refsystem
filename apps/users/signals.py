from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.invites.models import InviteCode
from apps.users.models import UserProfile, User
import random
import string


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserProfile)
def generate_invite_code(sender, instance, created, **kwargs):
    if created:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        InviteCode.objects.create(code=code, user=instance.user)
