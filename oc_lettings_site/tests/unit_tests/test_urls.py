"""Unit tests related to the URLs of the project."""

import pytest
import sentry_sdk
from django.urls import resolve, Resolver404
from oc_lettings_site.views import index


@pytest.fixture()
def stop_sentry():
    """Stop Sentry from sending events during tests."""
    sentry_sdk.init(dsn="")


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


def test_non_existent_url(client, stop_sentry):
    """Test that a non-existent URL resolves to a 404."""
    url = "/non-existent-url/"
    with pytest.raises(Resolver404):
        resolve(url).func
