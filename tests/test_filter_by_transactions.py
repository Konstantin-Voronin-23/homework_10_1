import re

from src.filter_by_transactions import get_filter_by_category, get_filter_by_string

TEST_TRANSACTIONS = [
    {
        "id": 441945886,
        "description": "Перевод организации",
    },
    {
        "id": 41428829,
        "description": "Перевод организации",
    },
    {
        "id": 939719570,
        "description": "Открытие вклада",
    },
    {
        "id": 123456789,
        "description": None,
    },
    {
        "id": 987654321,
    }
]


# Тесты для функции get_filter_by_string


def test_get_filter_by_string_valid() -> None:
    """Тест успешной отработки функции"""

    result = get_filter_by_string(TEST_TRANSACTIONS, "перевод")
    assert len(result) == 2
    assert result[0]["id"] == 441945886
    assert result[1]["id"] == 41428829


def test_get_filter_by_string_not_str() -> None:
    """Тест если строка поиска не строка"""

    try:
        get_filter_by_string(TEST_TRANSACTIONS, 123)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Строка поиска должна быть текстом"


def test_get_filter_by_string_empty() -> None:
    """Тест если в строку поиска ничего не написали"""

    try:
        get_filter_by_string(TEST_TRANSACTIONS, "")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Нужно ввести текст для сортировки списка транзакций"


def test_get_filter_by_string_not_list() -> None:
    """Тест когда первый аргумент не является списком"""

    try:
        get_filter_by_string({"id": 1}, "перевод")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Первый аргумент должен быть списком словарей"


def test_get_filter_by_string_runtime_error(monkeypatch) -> None:
    """Тест если при работе функции внутренняя ошибка RuntimeError"""

    broken_transaction = [{"description": "Normal description"}]

    def mock_search(*args, **kwargs):
        raise Exception("Internal error during search")

    monkeypatch.setattr(re, 'search', mock_search)
    try:
        get_filter_by_string(broken_transaction, "text")
        assert False, "Ожидалось RuntimeError"
    except RuntimeError as e:
        assert "В процессе произошла ошибка" in str(e)
        assert "Internal error during search" in str(e)


# Тесты для функции get_filter_by_category


def test_get_filter_by_category_valid() -> None:
    """Тест успешной отработки функции"""

    transactions = [
        {"description": "Перевод организации"},
        {"description": "Покупка в магазине"},
        {"description": "Перевод другу"},
    ]
    categories = ["перевод", "магазин"]
    result = get_filter_by_category(transactions, categories)
    assert result == {"перевод": 2, "магазин": 1}, "Неверный подсчет операций"


def test_get_filter_by_category_not_list_arg_1() -> None:
    """Тест если первый аргумент не является списком"""

    try:
        get_filter_by_category("not a list", ["перевод"])
        assert False, "Должно вызываться исключение ValueError для неверного типа transactions"
    except ValueError as e:
        assert str(e) == "Первый аргумент должен быть списком словарей", "Неверное сообщение об ошибке"


def test_get_filter_by_category_not_list_arg_2() -> None:
    """Тест если второй аргумент не является списком"""

    try:
        get_filter_by_category([], "not a list")
        assert False, "Должно вызываться исключение ValueError для неверного типа categories"
    except ValueError as e:
        assert str(e) == "Категории должны быть списком", "Неверное сообщение об ошибке"


def test_get_filter_by_category_empty():
    """Тест если в список категорий ничего не передали"""

    try:
        get_filter_by_category([], [])
        assert False, "Должно вызываться исключение ValueError для пустого списка категорий"
    except ValueError as e:
        assert str(e) == "Список категорий не может быть пустым", "Неверное сообщение об ошибке"


def test_get_filter_by_category_runtime_error():
    """Тест если при работе функции внутренняя ошибка RuntimeError"""

    broken_transaction = [{"description": {"unexpected": "type"}}]
    categories = ["test"]

    try:
        get_filter_by_category(broken_transaction, categories)
        assert False, "Ожидалось RuntimeError"
    except RuntimeError as e:
        assert "В процессе произошла ошибка" in str(e)
