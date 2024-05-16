"""Unit tests related to the URLs of the project."""

import pytest
from django.urls import resolve, Resolver404
from oc_lettings_site.views import index


def test_index_url_resolves(client):
    """Test that the index URL resolves to the index view."""
    url = "/"
    view = resolve(url).func
    assert view == index


def test_admin_url_resolves(client):
    """Test that the admin URL resolves to the admin view."""
    url = "/admin/"
    view = resolve(url).func
    assert view.__module__ == "django.contrib.admin.sites"


def test_non_existent_url(client):
    """Test that a non-existent URL resolves to a 404."""
    url = "/non-existent-url/"
    with pytest.raises(Resolver404):
        resolve(url).func
