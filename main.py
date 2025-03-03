from src.masks import get_mask_account, get_mask_card_number

# Данные от пользователя
user_card = input("Введите номер карты: ")
user_account = input("Введите номер счета: ")

result_card = get_mask_card_number(user_card)
result_account = get_mask_account(user_account)

print(result_card)
print(result_account)
