from typing import Iterator, Any


def filter_by_currency(transactions: list[dict[Any]], currency: str="USD") -> list[dict]:
    """Функция перебора списка словарей, она принимает на вход список словарей и возвращает,
    итератор который выдает транзакции если они соответствуют заданной валюте"""

    return [x for x in transactions if x.get("operationAmount", {}).get("currency", {}).get("name") == currency]

transactions = []
usd_transactions = iter(filter_by_currency(transactions, "USD"))
for _ in range(2):
    try:
        print(next(usd_transactions))
    except StopIteration:
        print("Больше нет данных")
        break


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция для генератора списков, которая принимает на вход список словарей и возвращает описание каждой
    операции по очереди"""

    for transaction in transactions:
        yield transaction.get("description")


transactions = []
descriptions = transaction_descriptions(transactions)

for _ in range(5):
    try:
        print(next(descriptions))
    except StopIteration:
        print("Больше нет данных")
        break


def card_number_generator(start: int, end: int) -> int:
    """Функция для генератора номеров банковских карт, который принимает на вход начальное и конечное значение
    карт в формате XXXX XXXX XXXX XXXX, где X— цифра номера карты и возвращает номера корт"""
    if start > end:
        raise ValueError("Стартовое значение не может быть больше конечного")

    for num in range(start, end + 1):
        full_number_card_gen = f"{num:016d}"
        part1 = full_number_card_gen[:4]
        part2 = full_number_card_gen[4:8]
        part3 = full_number_card_gen[8:12]
        part4 = full_number_card_gen[12:16]
        yield f"{part1} {part2} {part3} {part4}"

for card in card_number_generator(1, 10):
    print(card)
