from typing import Any, Dict, List, Optional, Union

from src.masks import get_mask_account, get_mask_card_number

# Переменные для аннотации

account_type = List[tuple[Union[str, None, list, Dict[Any, Any], float], Union[str, None]]]

# Тесты для функции get_mask_card_number


def test_mask_card_number_basic(card_basic: List[tuple[str, str]]) -> None:
    for user_card, expected in card_basic:
        assert get_mask_card_number(user_card) == expected


def test_mask_card_number_average(card_avarage: List[tuple[str, None]]) -> None:
    for user_card, expected in card_avarage:
        assert get_mask_card_number(user_card) == expected


def test_mask_card_number_advance(card_advance: List[tuple[Optional[str], None]]) -> None:
    for user_card, expected in card_advance:
        assert get_mask_card_number(user_card) == expected


# Тесты для функции get_mask_account

def test_get_mask_account_basic(account_basic: List[tuple[Union[str, int], Union[int, str]]]) -> None:
    for user_account, expected in account_basic:
        assert get_mask_account(user_account) == expected


def test_get_mask_account_average(account_avarage: List[tuple[Union[str, int, None], Union[None]]]) -> None:
    for user_account, expected in account_avarage:
        assert get_mask_account(user_account) == expected


def test_get_mask_account_advance(account_advance: account_type) -> None:
    for user_account, expected in account_advance:
        assert get_mask_account(user_account) == expected
