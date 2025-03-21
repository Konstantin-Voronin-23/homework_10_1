import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card_basic(mask_card_basic):
    for user_card, expected in mask_card_basic:
        assert mask_account_card(user_card) == expected

def test_mask_account_card_avarage(mask_card_average):
    for user_card, expected in mask_card_average:
        assert mask_account_card(user_card) == expected

@pytest.mark.parametrize("card", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
    ("Счет 12345678901234567890", "Счет 7890"),
    ("Amex 3782 8224 6310 005", "Некорретный номер!!!"),
    ("Счет 1234567890123456789", "Некорретный номер!!!"),
])
def test_mask_account_card_advance(card):
    user_card,expected = card
    assert mask_account_card(user_card) == expected

def test_get_date_basic(date_basic):
    for date, expected in date_basic:
        assert get_date(date) == expected

def test_get_date_average(date_average):
    for date in date_average:
        with pytest.raises(IndexError):
            get_date(date)

@pytest.mark.parametrize("date", [
        ("2023-01-01", "01.01.2023"),
        ("9999-12-31",  "31.12.9999")
    ])
def test_get_date_advance(date):
    user_date, expected = date
    assert get_date(user_date) == expected


