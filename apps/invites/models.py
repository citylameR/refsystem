from django.db import models

from apps.users.models import UserProfile as User


class InviteCode(models.Model):
    code = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey(User, related_name='invite_codes', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Invite code {self.code}"
