import pandas as pd
import csv
from typing import Union, List, Dict


def read_csv_file(file_path: str, delimiter: str = ";") -> List[Dict[str, Union[str, int, float]]]:
    """Читает CSV-файл.
    Принимает на вход путь к csv файлу и разделитель по умолчанию запятая.
    Возвращает список словарей, где ключ строка, а значение строка | целое число | дробное число """

    if not file_path:
        raise ValueError("Нужно указать путь к файлу")
    result = []

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            for row in reader:
                try:
                    print(row)
                except (ValueError, KeyError) as error:
                    print(f"Ошибка обработки строки{row}: {error}")
    except FileNotFoundError as error:
        print(f"Файл не найден {error}")
    except UnicodeDecodeError as error:
        print(f"Ошибка декодирования файла, попробуйте другую кодировку {error}")


def read_excel_file(file_path: str):
    pass
