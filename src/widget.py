from typing import Union


def mask_account_card(card: Union[str]) -> Union[str]:
    """ Функция для отображения номеров карт и счета"""
    card_split = card.split()
    card_and_account_type = ' '.join(card_split[:-1]) # Тип карты/Счет
    card_and_account_number = card_split[-1] # Номер карты/Счета
    card_len = 16
    account_len = 20
    if len(card_and_account_number) == card_len:
        mask_number = f"{card_and_account_type} {card_and_account_number[:4]} {card_and_account_number[4:6]}** **** {card_and_account_number[-4:]}"
        return mask_number

    elif len(card_and_account_number) == account_len:
        mask_number = f"Счет **{card_and_account_number[-4:]}"
        return mask_number
    return "Некорретный номер!!!"

# users_number_card = input("Введите номер карты: ")
# users_account_card = input("Введите номер счета: ")
#
# result_numbers = mask_account_card(users_number_card)
# result_account = mask_account_card(users_account_card)
#
# print(result_numbers)
# print(result_account)


date_input = str(input("Введите дату: "))

def get_date(date: Union[str]) -> Union[str]:
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"

result = get_date(date_input)
print(result)







