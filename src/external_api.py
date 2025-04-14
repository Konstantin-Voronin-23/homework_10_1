import os
from typing import Dict, Union

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL', "https://api.apilayer.com/exchangerates_data/convert")


def currency_conversion(transaction: Dict[str, Union[str, float]]) -> float:
    """Функция конвертации валюты из USD и EUR в рубли"""
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB')

    try:
        amount_float = float(amount)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Некорректная сумма: {amount}") from e

    if currency == "RUB":
        return amount_float

    if currency not in ("USD", "EUR"):
        raise ValueError(f"Некорректная валюта {currency}")

    try:
        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/convert",
            params={
                'base': currency,
                'symbols': 'RUB'
            },
            headers={'apikey': API_KEY},
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        if 'result' in data:
            return float(data['result'])
        elif 'rates' in data and 'RUB' in data['rates']:
            return amount_float * float(data['rates']['RUB'])
        else:
            raise ValueError(f"Некорректный ответ от API: {data}")

    except RequestException as error:
        raise ValueError(f"Ошибка при запросе к API: {error}") from error
