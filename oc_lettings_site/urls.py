"""oc_lettings_site URL Configuration, used as ROOT_URLCONF."""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("demo-logs/", views.demo_logs, name="demo_logs"),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path("admin/", admin.site.urls),
]
