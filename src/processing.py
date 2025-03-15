# Создание функций проекта
from typing import List


def filter_by_state(my_list: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """
    Функция фильтрации списков словарей по ключу
    """
    return [i for i in my_list if i['state'] == state]


def sort_by_date(my_list: List[dict], reversed_sorted: bool = True) -> List[dict]:
    """
    Функция сортировки даты по ключу
    """
    return sorted(my_list, key=lambda date: date.get("date", 0), reverse=reversed_sorted)
