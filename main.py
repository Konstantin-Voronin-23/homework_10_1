# Импорты модулей
from datetime import datetime
from typing import Dict, List

from config import PATH_TO_CSV, PATH_TO_EXCEL, PATH_TO_JSON
from src.csv_excel_file_reader import read_csv_file, read_excel_file
from src.filter_by_transactions import get_filter_by_string
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file


def get_user_choice(question: str, options: List[str]) -> str:
    """Получение выбора пользователя"""
    while True:
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = input("Ваш выбор (введите номер): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("⚠️ Неверный ввод. Пожалуйста, выберите номер из предложенных вариантов.")


def ask_yes_no(question: str) -> bool:
    """Запрос ответа Да/Нет"""
    while True:
        answer = input(f"\n{question} (да/нет): ").lower().strip()
        if answer in {'да', 'д'}:
            return True
        elif answer in {'нет', 'н'}:
            return False
        print("⚠️ Пожалуйста, введите 'да' или 'нет'")


def print_transactions(transactions: List[Dict]) -> None:
    """Вывод транзакций в удобном формате"""
    if not transactions:
        print("\nНе найдено транзакций, соответствующих условиям")
        return

    print("\nРезультаты фильтрации:")
    print("=" * 50)
    for t in transactions:
        try:
            # Форматирование даты
            date = datetime.fromisoformat(t['date']).strftime('%d.%m.%Y')
            description = t['description']

            # Получение суммы и валюты (для разных форматов)
            amount = t.get('amount') or t.get('operationAmount', {}).get('amount', 'N/A')
            currency = t.get('currency') or t.get('operationAmount', {}).get('currency', {}).get('name', '')

            # Вывод информации о транзакции
            print(f"\n{date} {description}")
            if 'from' in t:
                print(f"{t['from']} -> {t['to']}")
            else:
                print(f"Счет {t['to']}")
            print(f"Сумма: {amount} {currency}")

        except Exception as e:
            print(f"\nОшибка при выводе транзакции: {str(e)}")
    print("=" * 50)


def select_data_source() -> List[Dict]:
    """Выбор источника данных"""
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите источник данных:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")

    while True:
        choice = input("Ваш выбор (1-3): ").strip()
        if choice == '1':
            print("Для обработки выбран JSON-файл.")
            return read_json_file(PATH_TO_JSON)
        elif choice == '2':
            print("Для обработки выбран CSV-файл.")
            return read_csv_file(PATH_TO_CSV)
        elif choice == '3':
            print("Для обработки выбран XLSX-файл.")
            return read_excel_file(PATH_TO_EXCEL)
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3")


def main() -> None:
    """Функции для запуска проекта"""
    transactions = select_data_source()

    if not transactions:
        print("Не удалось загрузить транзакции")
        return

    state = get_user_choice(
        "Выберите статус для фильтрации:",
        ["EXECUTED", "CANCELED", "PENDING"]
    )
    filtered = filter_by_state(transactions, state)
    print(f"\nФильтр: статус '{state}' | Найдено операций: {len(filtered)}")

    if ask_yes_no("Отсортировать операции по дате?"):
        direction = get_user_choice(
            "Выберите направление сортировки:",
            ["По возрастанию (от старых к новым)", "По убыванию (от новых к старым)"]
        )
        reverse = direction.startswith("По убыванию")
        filtered = sort_by_date(filtered, reverse)
        print(f"\nСортировка: {direction}")
    else:
        print("\nСортировка по дате не применена")

    if ask_yes_no("Выводить только рублевые транзакции?"):
        filtered = filter_by_currency(filtered, "RUB")
        print("\nФильтр: только RUB")
    else:
        print("\nФильтр по валюте не применен")

    if ask_yes_no("Фильтровать по ключевому слову в описании?"):
        search_string = input("\nВведите слово для поиска:").strip()
        if search_string:
            filtered = get_filter_by_string(filtered, search_string)
            print(f"\nФильтр: описания содержат '{search_string}'")
        else:
            print("\nПустой запрос - фильтр не применен")
    else:
        print("\nФильтр по описанию не применен")

    print("\n" + "=" * 50)
    print_transactions(filtered)
    print("=" * 50)


if __name__ == "__main__":
    main()
