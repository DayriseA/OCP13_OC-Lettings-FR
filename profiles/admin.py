"""Admin configuration for the profiles app."""

from django.contrib import admin

from .models import Profile

# Register your models here.
admin.site.register(Profile)
