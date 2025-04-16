# Создание функций проекта
from typing import List


def filter_by_state(my_list: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """
    Функция фильтрации списков словарей по ключу
    """
    if not isinstance(my_list, list):
        print("ожидается список транзакций")
        return []

    try:
        return [t for t in my_list if t.get('state') == state]
    except AttributeError:
        return []


def sort_by_date(my_list: List[dict], reversed_sorted: bool = True) -> List[dict]:
    """
    Функция сортировки даты по ключу
    """
    if not isinstance(my_list, list):
        print("ожидается список транзакций")
        return

    return sorted(my_list, key=lambda date: date.get("date", 0), reverse=reversed_sorted)
