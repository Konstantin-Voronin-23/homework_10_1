# Создание функций проекта
from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Фильтрация транзакций по статусу"""
    if not isinstance(transactions, list):
        return []

    return [t for t in transactions if isinstance(t, dict) and t.get('state') == state]


def sort_by_date(my_list: List[Dict[str, Any]], reversed_sorted: bool = True) -> List[Dict[str, Any]]:
    """
    Функция сортировки даты по ключу
    """
    if not isinstance(my_list, list):
        print("ожидается список транзакций")
        return []

    def get_date_key(item: Dict[str, Any]) -> str:
        date_str: str = item.get("date", "")
        return date_str if date_str else "0000-00-00"

    return sorted(my_list, key=get_date_key, reverse=reversed_sorted)
