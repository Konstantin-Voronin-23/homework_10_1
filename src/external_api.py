import os
from typing import Dict, Union

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL', "https://api.apilayer.com/exchangerates_data/convert")


def currency_conversion(transaction: Dict[str, Union[str, float]]) -> float:
    """Функция конвертации валюты из USD и EUR в рубли"""
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB')

    if not isinstance(amount, (int, float)):
        raise ValueError(f"Некорректная сумма: {amount}")

    if currency == "RUB":
        return float(amount)

    if currency not in ("USD", "EUR"):
        raise ValueError(f"Некорректная валюта {currency}")

    try:
        response = requests.get(
            BASE_URL,
            params={
                'from': currency,
                'to': 'RUB',
                'amount': amount
            },
            headers={'apikey': API_KEY},
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        converted_amount = data.get('result')

        if converted_amount is None:
            raise ValueError(f"Некорректный ответ от API: {data}")

        return float(converted_amount)

    except requests.exceptions.RequestException as error:
        raise ValueError(f"Ошибка при запросе курса валют: {error}") from error
