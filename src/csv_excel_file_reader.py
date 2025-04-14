import pandas as pd
import csv
from typing import Union, List, Dict


def read_csv_file(file_path: str, delimiter: str = ";") -> List[Dict[str, Union[str, int, float]]]:
    """Читает CSV-файл.
    Принимает на вход путь к csv файлу и разделитель по умолчанию запятая.
    Возвращает список словарей, где ключ строка, а значение строка | целое число | дробное число """

    if not file_path:
        raise ValueError("Нужно указать путь к файлу")

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


def read_excel_file(file_path: str) -> List[Dict[str, Union[str, int, float]]]:
    """Читает excel-файл.
    Принимает на вход путь к excel файлу.
    Возвращает список словарей, где ключ строка, а значение строка | целое число | дробное число"""

    if not file_path:
        raise ValueError("Нужно указать путь к файлу")

    try:
        df = pd.read_excel(file_path)
        result_dict = df.to_dict(orient="records")
        return result_dict

    except Exception as error:
        raise Exception(f"Ошибка при чтении Excel файла{file_path}: {str(error)}")
