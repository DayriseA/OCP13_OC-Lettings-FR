"""pytest fixtures for the lettings app."""

import pytest
from lettings.models import Address, Letting


@pytest.fixture
def address(db):
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
    return Letting.objects.create(title="My super nice letting", address=address)
