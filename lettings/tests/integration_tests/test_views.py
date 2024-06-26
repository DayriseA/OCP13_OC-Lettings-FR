"""Integration tests for the views in the lettings app."""

import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view_uses_correct_template(client):
    """Test that the index view uses the correct template."""
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_view_uses_correct_template(client, letting):
    """Test that the letting view uses the correct template."""
    response = client.get(reverse("lettings:letting", args=[1]))
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_letting_view_with_non_existent_letting_returns_404(client, letting):
    """Test that a 404 status code is returned with a non-existent letting."""
    response = client.get(reverse("lettings:letting", args=[0]))
    assert response.status_code == 404
