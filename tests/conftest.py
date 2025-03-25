from typing import Any, Dict, List, Optional, Union

import pytest


@pytest.fixture
def card_basic() -> List[tuple[str, str]]:
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210123456", "9876 54** **** 3456")
    ]


@pytest.fixture
def card_avarage() -> List[tuple[str, None]]:
    return [
        ("123456", None),
        ("12345678901234567890", None),
        ("", None)
    ]


@pytest.fixture
def card_advance() -> List[tuple[Optional[str], None]]:
    return [
        (None, None),
        ("1234 5678 9012 3456", None),
        ("12.34567890123456", None)
    ]


@pytest.fixture
def account_basic() -> List[tuple[Union[str, int], Union[int, str]]]:
    return [
        (12345678901234567890, "**** **** **** **** 7890"),
        ("12345678901234567890", "**** **** **** **** 7890")
    ]


@pytest.fixture
def account_avarage() -> List[tuple[Union[str, int, None], Union[None]]]:
    return [
        ("12345", None),
        ("1234567890123456789", None),
        (123456789012345678901, None),
        (0, None),
        ("0", None)
    ]


@pytest.fixture
def account_advance() -> List[tuple[Union[str, None, list, Dict[Any, Any], float], Union[str, None]]]:
    return [
        (None, None),
        ([], None),
        ({}, None),
        (1234567890123456789.5, None)
    ]


@pytest.fixture
def mask_card_basic() -> List[tuple[str, str]]:
    return [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
        ("Счет 12345678901234567890", "Счет 7890"),
        ("Счет 12345123451234512345", "Счет 2345")
    ]


@pytest.fixture
def mask_card_average() -> List[tuple[str, str]]:
    return [
        ("Visa 123", "Некорретный номер!!!"),
        ("Счет 1234567890123456789", "Некорретный номер!!!"),
        ("", "Некорретный номер!!!"),
        ("Visa 1234567890123456@", "Некорретный номер!!!"),
        ("Visa 12345678abcd3456", "Некорретный номер!!!")
    ]


@pytest.fixture
def date_basic() -> List[tuple[str, str]]:
    return [
        ("2023-10-15", "15.10.2023"),
        ("2000-01-01", "01.01.2000"),
        ("1999-12-31", "31.12.1999")
    ]


@pytest.fixture
def date_average() -> List[str]:
    return [
        ("2023-10"),
        ("2023/10/15"),
        ("")
    ]


@pytest.fixture
def filter_by_state_basic() -> List[dict[str, Union[str, int]]]:
    return [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'PENDING'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 4, 'state': 'FAILED'},
        {'id': 5, 'state': 'EXECUTED'},
    ]


@pytest.fixture
def datatime_basic() -> List[dict[str, Union[str, int]]]:
    return [
        {'id': 1, 'date': '2023-10-01'},
        {'id': 2, 'date': '2023-09-15'},
        {'id': 3, 'date': '2023-10-01'},
        {'id': 4, 'date': '2023-08-25'},
        {'id': 5, 'date': '2023-09-20'},
    ]


@pytest.fixture
def currency_basic() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
        ]



@pytest.fixture
def currency_average() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2023-05-15T14:22:10.123456",
            "operationAmount": {
                "amount": "15000.50",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 1234 5678 9012 3456",
            "to": "MasterCard 9876 5432 1098 7654"
        },
        {
            "id": 987654321,
            "state": "CANCELED",
            "date": "2022-11-30T09:45:33.789012",
            "operationAmount": {
                "amount": "500.00",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Оплата услуг",
            "from": "Счет 12345678901234567890",
            "to": "Счет 98765432109876543210"
        }
    ]
