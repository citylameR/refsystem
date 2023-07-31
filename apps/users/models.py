# models.py
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User

from apps.invites.models import InviteCode as Ivite


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)
    invite_codes = GenericRelation(Ivite)

    def __str__(self):
        return self.user.get_full_name()


class VerificationCode(models.Model):
    phone_number = models.CharField(max_length=15)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Code {self.code} for {self.phone_number}"
