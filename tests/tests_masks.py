from src.masks import get_mask_account, get_mask_card_number

def test_mask_card_number_basic(card_basic):
    for user_card, expected in card_basic:
        assert get_mask_card_number(user_card) == expected


def test_mask_card_number_average(card_avarage):
    for user_card, expected in card_avarage:
        assert get_mask_card_number(user_card) == expected


def test_mask_card_number_advance(card_advance):
    for user_card, expected in card_advance:
        assert get_mask_card_number(user_card) == expected


def test_get_mask_account_basic(account_basic):
    for user_account, expected in account_basic:
        assert get_mask_account(user_account) == expected


def test_get_mask_account_average(account_avarage):
    for user_account, expected in account_avarage:
        assert get_mask_account(user_account) == expected


def test_get_mask_account_advance(account_advance):
    for user_account, expected in account_advance:
        assert get_mask_account(user_account) == expected

