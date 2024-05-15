"""URL configuration for profiles app."""

from django.urls import path

from . import views

app_name = "profiles"  # Set the application namespace
urlpatterns = [
    path("profiles/", views.index, name="index"),
    path("profiles/<str:username>/", views.profile, name="profile"),
]
