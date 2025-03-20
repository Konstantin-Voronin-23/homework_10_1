import pytest

# Фикстуры для get_mask_card_number
@pytest.fixture
def card_basic():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210123456", "9876 54** **** 3456")
    ]

@pytest.fixture
def card_avarage():
    return [
        ("123456", None),
        ("12345678901234567890", None),
        ("", None)
    ]

@pytest.fixture
def card_advance():
    return [
        (None, None),
        ("1234 5678 9012 3456", None),
        ("12.34567890123456", None)
    ]

# Фикстуры для get_mask_account
@pytest.fixture
def account_basic():
    return [
        (12345678901234567890, "**** **** **** **** 7890"),
        ("12345678901234567890", "**** **** **** **** 7890")
    ]

@pytest.fixture
def account_avarage():
    return [
        ("12345", None),
        ("1234567890123456789", None),
        (123456789012345678901, None),
        (0, None),
        ("0", None)
    ]

@pytest.fixture
def account_advance():
    return [
        (None, None),
        ([],None),
        ({}, None),
        (1234567890123456789.5, None)
    ]
