import re
import json
from typing import List, Dict, Any
from config import PATH_TO_JSON


def get_filter_by_string(file_path: str, search_string: str) -> List[Dict[str, Any]]:
    """Функция которая принимает на вход список словарей и строку поиска, а на выход отдает список словарей
    у которых в описании есть данныя строка"""

    if not isinstance(search_string, str):
        raise ValueError("Строка поиска должна быть текстом")
    if not search_string.strip():
        raise ValueError("Нужно ввести текст для сортировки списка транзакций")

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            transaction = json.load(json_file)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Файл не найден {file_path}") from error
    try:
        return [operation for operation in transaction
                if operation.get("description")
                and re.search(search_string, operation.get('description'), re.IGNORECASE)]
    except Exception as error:
        raise RuntimeError(f"В процессе произошла ошибка {error}")


# Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
# а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
# Категории операций хранятся в поле description
def get_filter_by_category(file_path: str, categories: list[str]) -> Dict[str, Any]:

    if not isinstance(categories, list):
        raise ValueError("Категории должны быть списком")
    if not categories:
        raise ValueError("Список категорий не может быть пустым")
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            transactions = json.load(json_file)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Файл не найден {file_path}") from error
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
