import logging
from typing import Any, Dict, Optional, Union

logger = logging.getLogger("masks")
file_handler = logging.FileHandler('../logs/masks.log', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(user_card: Optional[str]) -> Union[str, None]:
    """
    Функция маскировки номера банковской карты
    """
    logger.info(f"Запуск функции маскировки номера банковской карты с аргументом: {user_card}")
    if not user_card:
        logger.warning("Получен пустой номер карты")
        return None

    try:
        user_card_string = str(user_card).strip()
        if not user_card_string.isdigit():
            logger.error(f"Номер карты содержит не числовые символы {user_card}")
            return None

        card_len = 16
        if len(user_card_string) != card_len:
            logger.error(f"Длина карты не соответствует: {len(user_card_string)} - ожидалось{card_len}")
            return None

        masked_number = f"{user_card_string[:4]} {user_card_string[4:6]}** **** {user_card_string[-4:]}"
        logger.info(f"Успещная маскировка карты: {masked_number}")
        return masked_number
    except Exception as error:
        logger.error(f"Ошибка при маскировке карты {error}", exc_info=True)
        return None


def get_mask_account(user_account: Union[str, int, None, list, Dict[Any, Any], float]) -> Union[str, None]:
    """
    Функция маскировки номера банковского счета
    """
    logger.info(f"Запуск функции маскировки номера банковского счета с аргументом: {user_account}")
    if user_account is None:
        logger.warning("Получен пустой номер банковского счета")
        return None

    try:
        user_account_string = str(user_account).strip()
        if not user_account_string.isdigit():
            logger.error(f"Номер банковского счета содержит не числовые символы {user_account}")
            return None

        account_len = 20
        if len(user_account_string) != account_len:
            logger.error(f"Длина счета не соответствует: {len(user_account_string)} - ожидалось {account_len}")
            return None

        masked_account = f"**** **** **** **** {user_account_string[-4:]}"
        logger.info(f"Успешная маскировка банковского счета{masked_account}")
        return masked_account
    except Exception as error:
        logger.error(f"Ошибка при маскировке банковского счета {error}", exc_info=True)
        return None
