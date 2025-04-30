import re
from typing import Any, Dict, List, Optional


def get_filter_by_string(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход список словарей и строку поиска, а на выход отдает
    список словарей, у которых в описании есть данная строка (без учета регистра)."""

    if not isinstance(search_string, str):
        raise ValueError("Строка поиска должна быть текстом")
    if not search_string.strip():
        raise ValueError("Нужно ввести текст для сортировки списка транзакций")
    if not isinstance(transactions, list):
        raise ValueError("Первый аргумент должен быть списком словарей")

    try:
        filtered_transactions: List[Dict[str, Any]] = []
        for operation in transactions:
            description: Optional[str] = operation.get("description")
            if description and isinstance(description, str):
                if re.search(search_string, description, re.IGNORECASE):
                    filtered_transactions.append(operation)
        return filtered_transactions
    except Exception as error:
        raise RuntimeError(f"В процессе произошла ошибка: {error}")


def get_filter_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, Any]:
    """Функция которая принимает список словарей и список категорий, а возвращает словарь
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""

    if not isinstance(categories, list):
        raise ValueError("Категории должны быть списком")
    if not categories:
        raise ValueError("Список категорий не может быть пустым")
    if not isinstance(transactions, list):
        raise ValueError("Первый аргумент должен быть списком словарей")

    try:
        result_dict = {category: 0 for category in categories}
        for transaction in transactions:
            description = transaction.get('description', '')
            for category in categories:
                if category.lower() in description.lower():
                    result_dict[category] += 1
        return result_dict
    except Exception as error:
        raise RuntimeError(f"В процессе произошла ошибка {error}")
