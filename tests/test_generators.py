import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

from typing import Iterator, Any

# Тесты для функции filter_by_currency


def test_filter_by_currency_valid(currency_basic: list[dict[Any]], currency: str="USD") -> None:
    """Тест проверяющий, что функция корректно фильтрует транзакции по заданной валюте"""

    result = filter_by_currency(currency_basic, "USD")
    assert result == currency_basic


@pytest.mark.parametrize("currency, expected", [
    ("USD", 2),
    ("RUB", 1),
    ("EUR", 1),
    ("WON", 0)
])
def test_filter_by_currency_invalid(currency_average: list[dict[Any]], currency: str, expected: int) -> None:
    """Тест проверяющий, что функция корректно обрабатывает случаи когда не транзакции в заданной валюте
    отсутствуют"""

    result = filter_by_currency(currency_average, currency)
    assert len(result) == expected


def test_filter_by_currency_empty() -> None:
    """Тест проверяющий, что функция корректно обрабатывает случаи когда на вход приходит пустой список"""
    assert filter_by_currency([], "USD") == []


# Тесты для функции transaction_descriptions

def test_transaction_descriptions_valid(currency_average: list[dict[Any]]) -> None:
    """Тест проверяющий, что функция возвращает корректные описания для каждой транзакции"""

    expected_str = ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту", "Оплата услуг"]
    result = list(transaction_descriptions(currency_average))
    assert result == expected_str


@pytest.mark.parametrize("expected_description", [
    ["Перевод организации",
      "Перевод со счета на счет",
      "Перевод с карты на карту",
      "Оплата услуг"]
])
def test_transaction_descriptions(currency_average: list[dict[Any]], expected_description: list[str]) -> None:
    """Тест проверяющий работу функции генератора с различными входными данными"""

    generator = transaction_descriptions(currency_average)
    result = list(generator)
    assert result == expected_description


def test_transaction_descriptions_empty() -> None:
    """Тест проверяющий работу функции генератора с пустым списком"""

    assert list(transaction_descriptions([])) == []


# Тест для функции card_number_generator


def test_card_number_generator() -> None:
    """Тест проверяющий правильную работу генератора карт"""
    generator = card_number_generator(1, 1)
    assert next(generator) == "0000 0000 0000 0001"


def test_card_number_generator_range() -> None:
    """Тест проверяющий правильную работу заданного диапазона карт"""
    generator = card_number_generator(1, 5)
    numbers = list(generator)
    assert len(numbers) == 5
    assert numbers[0] == "0000 0000 0000 0001"
    assert numbers[-1] == "0000 0000 0000 0005"


def test_card_number_generator_min_max_value() -> None:
    """Тест проверяющий правильную работу минимального и максимального значения карт"""
    generator_min = card_number_generator(0, 0)
    generator_max = card_number_generator(9999999999999999, 9999999999999999)
    assert next(generator_min) == "0000 0000 0000 0000"
    assert next(generator_max) == "9999 9999 9999 9999"


def test_card_number_generator_invalid_range() -> None:
    """Тест проверяющий невалидный диапазон значения карты"""
    with pytest.raises(ValueError):
        list(card_number_generator(5, 1))

