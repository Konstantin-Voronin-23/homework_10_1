from unittest.mock import Mock, mock_open
from unittest.mock import patch
import pytest
import json
from src.utils import read_json_file

@patch("builtins.open", new_callable=mock_open)
def test_read_valid_json(mock_file) -> None:
    """Тест для проверки корректного JSON файла"""
    mock_data = [{"id": 1, "amount": 100}]
    mock_json = json.dumps(mock_data)
    mock_file.return_value.read.return_value = mock_json

    result = read_json_file("file.json")

    assert result == mock_data
    mock_file.assert_called_once_with("file.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open)
@patch("json.load")
def test_read_invalid_json(mock_json_load, mock_file) -> None:
    """Тест для проверки не корректного JSON файла, возвращает пустой список если выкидывает исключение"""
    mock_json_load.side_effect = json.JSONDecodeError("Expecting value", doc="", pos=0)

    result = read_json_file("fake.json")

    assert result == []
    mock_file.assert_called_once_with("fake.json", "r", encoding="utf-8")
