from unittest.mock import MagicMock, mock_open, patch

import pytest

from src.csv_excel_file_reader import read_csv_file, read_excel_file


def test_read_csv_file_valid() -> None:
    """Тест для проверки корректной работы функции """
    csv_content = (
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
        "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
        "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;"
        "Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту"
    )

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
    """Тест для проверки работы функции если не указан путь csv файла """
    with pytest.raises(ValueError, match="Нужно указать путь к файлу"):
        read_csv_file("")


def test_read_csv_file_empty() -> None:
    """Тест для проверки работы функции если csv файл пустой """
    csv_content = ""

    with patch("builtins.open", mock_open(read_data=csv_content)):
        result = read_csv_file("logsfile.csv")
        assert result == []


def test_read_excel_file_valid() -> None:
    """Тест для проверки функции с корректными данными из excel """
    expected_data = [
        {
            'id': 650703.0,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210.0,
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        },
        {
            'id': 3598919.0,
            'state': 'EXECUTED',
            'date': '2020-12-06T23:00:58Z',
            'amount': 29740.0,
            'currency_name': 'Peso',
            'currency_code': 'COP',
            'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643',
            'description': 'Перевод с карты на карту'
        }
    ]

    mock_df = MagicMock()
    mock_df.to_dict.return_value = expected_data

    with patch("pandas.read_excel", return_value=mock_df) as mock_read:
        result = read_excel_file("transactions_excel.xlsx")
        assert result == expected_data
        mock_read.assert_called_once_with("transactions_excel.xlsx")
        mock_df.to_dict.assert_called_once_with(orient="records")


def test_read_excel_file_invalid() -> None:
    """Тест для проверки функции с некорректными данными из excel """
    with patch("pandas.read_excel") as mock_read:
        mock_read.side_effect = Exception("Invalid file")
        with pytest.raises(Exception, match="Ошибка при чтении Excel файла invalid.xlsx: Invalid file"):
            read_excel_file("invalid.xlsx")


def test_read_excel_file_empty() -> None:
    """Тест для проверки работы функции если excel файл пустой"""
    with pytest.raises(ValueError, match="Нужно указать путь к файлу"):
        read_excel_file("")
