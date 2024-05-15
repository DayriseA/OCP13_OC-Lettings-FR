"""Models for the profiles app."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """A profile is related to a user and stores additional information."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
