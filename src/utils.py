import json
from typing import Dict, List


def read_json_file(file_path: str = "operations.json") -> List[Dict]:
    """Функция для чтения json файла с операциями транзакций"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден! ")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {file_path} содержит некорректный JSON! ")
        return []
