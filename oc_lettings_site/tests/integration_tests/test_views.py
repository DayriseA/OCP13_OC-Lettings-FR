"""Integration test related to the views of the project."""

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_index_view_uses_correct_template(client):
    """Test that the index view uses the correct template."""
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
