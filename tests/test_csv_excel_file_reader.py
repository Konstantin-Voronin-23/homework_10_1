import csv
import pandas as pd
import pytest
from unittest.mock import mock_open, patch
from src.csv_excel_file_reader import read_csv_file
from src.csv_excel_file_reader import read_excel_file
from config import PATH_TO_CSV, PATH_TO_EXCEL


def test_read_csv_file_valid() -> None:
    """Тест для проверки корректной работы функции"""
    csv_content = """id;state;date;amount;currency_name;currency_code;from;to;description
    650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
    3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту"""

    expected = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации"
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту"
        }
    ]

    with patch("builtins.open", mock_open(read_data=csv_content)):
        result = read_csv_file("transactions.csv", delimiter=";")
        assert result == expected


def test_read_csv_file_invalid() -> None:
    """Тест для проверки работы функции если не указан путь csv файла"""
    with pytest.raises(ValueError, match="Нужно указать путь к файлу"):
        read_csv_file("")


def test_read_csv_file_empty() -> None:
    """Тест для проверки работы функции если csv файл пустой"""
    csv_content = ""

    with patch("builtins.open", mock_open(read_data=csv_content)):
        result = read_csv_file("logsfile.csv")
        assert result == []
