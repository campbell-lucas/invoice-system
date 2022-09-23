from django.core.exceptions import ValidationError

from customers.models import Customer, validate_length


def test_validate_length():
    length = 7
    validate_length(length)
    assert ValidationError

