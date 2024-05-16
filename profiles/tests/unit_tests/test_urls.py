"""Unit tests related to the URLs of profiles app."""

from django.urls import resolve
from profiles.views import index, profile


def test_index_url_resolves(client):
    """Test that the index URL resolves to the index view."""
    url = "/profiles/"
    view = resolve(url).func
    assert view == index


def test_profile_url_resolves(client):
    """Test that the profile URL resolves to the profile view."""
    url = "/profiles/user/"
    view = resolve(url).func
    assert view == profile
