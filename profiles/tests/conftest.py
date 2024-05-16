"""pytest fixtures for the profiles app."""

import pytest
from profiles.models import Profile


# Since a user is needed to create a profile, we define a fixture to create a user.
@pytest.fixture
def test_user(db, django_user_model):
    return django_user_model.objects.create(username="testuser", password="testpwd")


@pytest.fixture
def profile(db, test_user):
    return Profile.objects.create(user=test_user, favorite_city="Springfield")
