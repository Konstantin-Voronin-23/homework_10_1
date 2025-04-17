import json
import logging
import os
from typing import Dict, List

log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log")
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_file(file_path: str = "../data/operations.json") -> List[Dict]:
    """Функция для чтения json файла с операциями транзакций"""
    logger.info(f"Запуск функции для чтения json файла с аргументом: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(f"Успешное чтение JSON файла {file_path}")
            if not isinstance(data, list):
                logger.warning(f"Данные в файле {file_path} не являются списком, возвращаем пустой список")
                return []
            return data
    except FileNotFoundError as error:
        print(f"Ошибка: файл {error.filename} не найден! ")
        logger.error(f"Ошибка, файл не найден {error}", exc_info=True)
        return []
    except json.JSONDecodeError as error:
        print(f"Ошибка: файл {file_path} содержит некорректный JSON! ")
        logger.error(f"Ошибка: файл содержит некорректный JSON: {error}", exc_info=True)
        return []
