import os
import requests
from dotenv import load_dotenv
from typing import Dict, Union

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')


def currency_conversion(transaction: Dict[str, Union[str, float]]) -> float:
    """Функция конвертации валюты из USD и EUR в рубли"""
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB')
    if currency == "RUB":
        return float(amount)
    if currency not in ("USD", "EUR"):
        raise ValueError(f"Некорректная валюта {currency} ")
    try:
        response = requests.get(
            BASE_URL,
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': API_KEY},
            timeout=10
        )
        response.raise_for_status()

        rates = response.json()['rates']
        rub_rate = rates['RUB']
        return float(amount) * rub_rate

    except requests.exceptions.RequestException as error:
        raise ValueError(f"Ошибка при запросе курса валют: {error}") from error
