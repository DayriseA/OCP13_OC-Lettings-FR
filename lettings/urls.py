"""URL configuration for lettings app."""

from django.urls import path

from . import views

app_name = "lettings"  # Set the application namespace
urlpatterns = [
    path("lettings/", views.index, name="index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
]
