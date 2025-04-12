import json
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


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
