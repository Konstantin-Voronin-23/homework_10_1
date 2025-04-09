from unittest.mock import Mock, patch

import pytest

from src.external_api import API_KEY, BASE_URL, currency_conversion


@patch("src.external_api.requests.get")
def test_currency_conversion_valid(mock_get) -> None:
    """Тест корректной конвертации USD -> RUB"""
    transaction = {"amount": 100, "currency": "USD"}

    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 90.0}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = currency_conversion(transaction)

    assert result == 9000.0
    mock_get.assert_called_once_with(
        BASE_URL,
        params={'base': 'USD', 'symbols': 'RUB'},
        headers={'apikey': API_KEY},
        timeout=10
    )


def test_currency_conversion_invalid_currency() -> None:
    """Тест некорректной работы, когда передана неизвестная по условию валюта"""
    transaction = {"amount": 100, "currency": "BTC"}

    with pytest.raises(ValueError) as exc_info:
        currency_conversion(transaction)

    assert "Некорректная валюта BTC" in str(exc_info.value)
