"""pytest fixtures for the lettings app."""

import pytest
import sentry_sdk
from lettings.models import Address, Letting


@pytest.fixture(autouse=True)
def stop_sentry():
    """Stop Sentry from sending events during tests."""
    sentry_sdk.init(dsn="")


@pytest.fixture
def address(db):
    """Create an Address object for testing."""
    return Address.objects.create(
        number=10,
        street="Main Street",
        city="Springfield",
        state="IL",
        zip_code=62701,
        country_iso_code="USA",
    )


@pytest.fixture
def letting(db, address):
    """Create a Letting object for testing."""
    return Letting.objects.create(title="My super nice letting", address=address)
