from typing import Any, Dict, Optional, Union


def get_mask_card_number(user_card: Optional[str]) -> Union[str, None]:
    """
    Функция маскировки номера банковской карты
    """
    card_len = 16
    user_card_string = str(user_card)

    if len(user_card_string) == card_len:
        return f"{user_card_string[:4]} {user_card_string[4:6]}** **** {user_card_string[-4:]}"
    return None


def get_mask_account(user_account: Union[str, int, None, list, Dict[Any, Any], float]) -> Union[str, None]:
    """
    Функция маскировки номера банковского счета
    """
    account_len = 20
    user_account_string = str(user_account)

    if len(user_account_string) == account_len:
        return f"**** **** **** **** {user_account_string[-4:]}"
    return None
