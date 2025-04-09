from typing import Dict, List, Union

import pytest

from src.processing import filter_by_state, sort_by_date

# Переменные для аннотации
filter_type = List[dict[str, Union[str, int]]]
expected_type = List[dict[str, Union[str, int]]]
# Тесты для функции filter_by_state


def test_filter_by_state_basic_one(filter_by_state_basic: List[dict[str, Union[str, int]]]) -> None:
    result = filter_by_state(filter_by_state_basic, "EXECUTED")
    expected = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 5, 'state': 'EXECUTED'},
    ]
    assert result == expected


def test_filter_by_state_basic_two(filter_by_state_basic: List[dict[str, Union[str, int]]]) -> None:
    result = filter_by_state(filter_by_state_basic, 'PENDING')
    expected = [{'id': 2, 'state': 'PENDING'}]
    assert result == expected


def test_filter_by_state_avarage(filter_by_state_basic: List[dict[str, Union[str, int]]]) -> None:
    result = filter_by_state(filter_by_state_basic, 'COMPLETED')
    expected: List[dict[str, Union[str, int]]] = []
    assert result == expected


@pytest.mark.parametrize("status, expected", [
    ('EXECUTED', [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}, {'id': 5, 'state': 'EXECUTED'}]),
    ('PENDING', [{'id': 2, 'state': 'PENDING'}]),
    ('FAILED', [{'id': 4, 'state': 'FAILED'}]),
    ('COMPLETED', []),
])
def test_filter_by_state_average(filter_by_state_basic: filter_type, status: str, expected: expected_type) -> None:
    result = filter_by_state(filter_by_state_basic, status)
    assert result == expected


# Тесты для функции sort_by_date


def test_sort_by_date_basic_one(datatime_basic: List[dict[str, Union[str, int]]]) -> None:
    result = sort_by_date(datatime_basic)
    expected = [
        {'id': 1, 'date': '2023-10-01'},
        {'id': 3, 'date': '2023-10-01'},
        {'id': 5, 'date': '2023-09-20'},
        {'id': 2, 'date': '2023-09-15'},
        {'id': 4, 'date': '2023-08-25'},
    ]
    assert result == expected


def test_sort_by_date_basic_two(datatime_basic: List[dict[str, Union[str, int]]]) -> None:
    result = sort_by_date(datatime_basic, reversed_sorted=False)
    expected = [
        {'id': 4, 'date': '2023-08-25'},
        {'id': 2, 'date': '2023-09-15'},
        {'id': 5, 'date': '2023-09-20'},
        {'id': 1, 'date': '2023-10-01'},
        {'id': 3, 'date': '2023-10-01'},
    ]
    assert result == expected


def test_sort_by_date_average(datatime_basic: List[dict[str, Union[str, int]]]) -> None:
    data_with_same_dates = [
        {'id': 1, 'date': '2023-10-01'},
        {'id': 2, 'date': '2023-10-01'},
        {'id': 3, 'date': '2023-09-15'},
    ]
    result = sort_by_date(data_with_same_dates)
    expected = [
        {'id': 1, 'date': '2023-10-01'},
        {'id': 2, 'date': '2023-10-01'},
        {'id': 3, 'date': '2023-09-15'},
    ]
    assert result == expected


def test_sort_by_date_advance() -> None:
    result = sort_by_date([])
    expected: List[Dict[str, Union[str, int]]] = []
    assert result == expected
