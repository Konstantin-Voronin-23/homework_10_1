from typing import Dict, List, Union


from src.processing import filter_by_state, sort_by_date

# Переменные для аннотации
filter_type = List[dict[str, Union[str, int]]]
expected_type = List[dict[str, Union[str, int]]]
# Тесты для функции filter_by_state


# Тесты для filter_by_state


def test_filter_executed(sample_transactions):
    result = filter_by_state(sample_transactions, 'EXECUTED')
    assert result == [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2023-09-20'},
    ]


def test_filter_pending(sample_transactions):
    result = filter_by_state(sample_transactions, 'PENDING')
    assert result == [{'id': 2, 'state': 'PENDING', 'date': '2023-09-15'}]


def test_filter_empty_result(sample_transactions):
    assert filter_by_state(sample_transactions, 'COMPLETED') == []


def test_filter_invalid_input():
    assert filter_by_state(None) == []
    assert filter_by_state("not a list") == []
    assert filter_by_state(123) == []


def test_filter_missing_state_key():
    data = [{'id': 1}, {'id': 2, 'state': 'EXECUTED'}]
    assert filter_by_state(data) == [{'id': 2, 'state': 'EXECUTED'}]


def test_filter_mixed_data_types():
    data = [{'id': 1, 'state': 'EXECUTED'}, "not a dict", 123]
    assert filter_by_state(data) == [{'id': 1, 'state': 'EXECUTED'}]


# Тесты для sort_by_date


def test_sort_default(sample_transactions):
    result = sort_by_date(sample_transactions)
    assert result == [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2023-09-20'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-09-15'},
        {'id': 4, 'state': 'FAILED', 'date': '2023-08-25'},
    ]


def test_sort_ascending(sample_transactions):
    result = sort_by_date(sample_transactions, False)
    assert result == [
        {'id': 4, 'state': 'FAILED', 'date': '2023-08-25'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-09-15'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2023-09-20'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-01'},
    ]


def test_sort_empty_list():
    assert sort_by_date([]) == []


def test_sort_invalid_input():
    assert sort_by_date(None) == []
    assert sort_by_date("not a list") == []
    assert sort_by_date(123) == []


def test_sort_missing_date_key():
    data = [
        {'id': 1, 'date': '2023-10-01'},
        {'id': 2},  # Нет даты
        {'id': 3, 'date': '2023-09-15'},
    ]
    assert sort_by_date(data) == [
        {'id': 1, 'date': '2023-10-01'},
        {'id': 3, 'date': '2023-09-15'},
        {'id': 2},
    ]
