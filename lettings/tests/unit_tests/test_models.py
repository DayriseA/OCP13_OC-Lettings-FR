"""Unit tests for the lettings app models."""

from lettings.models import Address, Letting


class TestAddress:
    """Tests for the Address model."""

    def test_address_creation(self, address):
        """Test that an address is correctly created."""
        assert isinstance(address, Address)
        assert address.number == 10
        assert address.street == "Main Street"
        assert address.city == "Springfield"
        assert address.state == "IL"
        assert address.zip_code == 62701
        assert address.country_iso_code == "USA"

    def test_address_str(self, address):
        """Test that the address string representation is correct."""
        assert str(address) == "10 Main Street"


class TestLetting:
    """Tests for the Letting model."""

    def test_letting_creation(self, letting):
        """Test that a letting is correctly created."""
        assert isinstance(letting, Letting)
        assert isinstance(letting.address, Address)
        assert letting.title == "My super nice letting"
        assert letting.address.street == "Main Street"

    def test_letting_str(self, letting):
        """Test that the letting string representation is correct."""
        assert str(letting) == "My super nice letting"
