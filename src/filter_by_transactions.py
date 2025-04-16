import re
import json
from typing import List, Dict, Any


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
