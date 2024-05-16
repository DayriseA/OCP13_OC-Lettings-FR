"""Integration tests for the views in the profiles app."""

import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view_uses_correct_template(client):
    """Test that the index view uses the correct template."""
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_view_uses_correct_template(client, test_user, profile):
    """Test that the profile view uses the correct template."""
    response = client.get(reverse("profiles:profile", args=[test_user.username]))
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profile_view_with_non_existent_user_raises_exception(client):
    """Test that ObjectDoesNotExist is raised with a non-existent user."""
    with pytest.raises(ObjectDoesNotExist):
        client.get(reverse("profiles:profile", args=["non_existent_user"]))
