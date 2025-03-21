from datetime import datetime


def mask_account_card(card: str) -> str:
    """ Функция для отображения номеров карт и счета"""

    card_split = card.split()

    if len(card_split) < 2:
        return "Некорретный номер!!!"

    card_and_account_type = ' '.join(card_split[:-1])
    card_and_account_number = card_split[-1].replace(" ", "")
    card_len = 16
    account_len = 20

    if not card_and_account_number.isdigit():
        return "Некорретный номер!!!"

    if len(card_and_account_number) == card_len:
        mask_number = (f"{card_and_account_type} {card_and_account_number[:4]}"
                       f" {card_and_account_number[4:6]}** **** {card_and_account_number[-4:]}")
        return mask_number

    elif len(card_and_account_number) == account_len:
        mask_number = f"Счет {card_and_account_number[-4:]}"
        return mask_number

    return "Некорретный номер!!!"


def get_date(date: str) -> str:
    """Функция изменения формата даты"""
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Неверный формат даты. Ожидается формат YYYY-MM-DD.")

    return date_obj.strftime("%d.%m.%Y")
