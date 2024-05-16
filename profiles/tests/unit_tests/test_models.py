"""Unit tests for the profiles app models."""

from profiles.models import Profile


class TestProfile:
    """Tests for the Profile model."""

    def test_profile_creation(self, profile):
        """Test that a profile is correctly created."""
        assert isinstance(profile, Profile)
        assert profile.favorite_city == "Springfield"

    def test_profile_str(self, profile):
        """Test that the profile string representation is correct."""
        assert str(profile) == "testuser"
