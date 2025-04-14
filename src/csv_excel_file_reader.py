import csv
from typing import Any, Dict, List, Union, cast

import pandas as pd


def read_csv_file(file_path: str, delimiter: str = ";") -> List[Dict[str, Union[Any]]]:
    """Читает CSV-файл.
    Принимает на вход путь к csv файлу и разделитель по умолчанию запятая.
    Возвращает список словарей, где ключ строка, а значение строка | целое число | дробное число """

    if not file_path:
        raise ValueError("Нужно указать путь к файлу")

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
            return [
                {k: v.strip() if isinstance(v, str) else v  # Очищаем пробелы
                for k, v in row.items()}
                for row in csv.DictReader(csv_file, delimiter=delimiter)
            ]

    except FileNotFoundError as error:
        raise FileNotFoundError(f"Файл не найден {error}")


def read_excel_file(file_path: str) -> List[Dict[str, Union[Any]]]:
    """Читает excel-файл.
    Принимает на вход путь к excel файлу.
    Возвращает список словарей, где ключ строка, а значение строка | целое число | дробное число"""

    if not file_path:
        raise ValueError("Нужно указать путь к файлу")

    try:
        df = pd.read_excel(file_path)
        return cast(List[Dict[str, Any]], df.to_dict(orient="records"))

    except Exception as error:
        raise Exception(f"Ошибка при чтении Excel файла {file_path}: {str(error)}")
