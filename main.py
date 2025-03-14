# from src.widget import get_date, mask_account_card

# Данные от пользователя
users_number_card = input("Введите номер карты: ")
users_account_card = input("Введите номер счета: ")
date_input = str(input("Введите дату: "))

result_numbers = mask_account_card(users_number_card)
result_account = mask_account_card(users_account_card)
result_date = get_date(date_input)

print(result_numbers)
print(result_account)
print(result_date)
