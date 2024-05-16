"""Unit tests related to the URLs of letting app."""

from django.urls import resolve
from lettings.views import index, letting


def test_index_url_resolves(client):
    """Test that the index URL resolves to the index view."""
    url = "/lettings/"
    view = resolve(url).func
    assert view == index


def test_letting_url_resolves(client):
    """Test that the letting URL resolves to the letting view."""
    url = "/lettings/1/"
    view = resolve(url).func
    assert view == letting
