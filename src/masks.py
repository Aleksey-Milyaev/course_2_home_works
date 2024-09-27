import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "masks.log"), "w")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int = 0) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info(f"маскировка номера карты: {card_number}")
    if card_number == 0:
        logger.info("Номер карты не введен")
        return "Номер карты не введен"
    card_number_string = str(card_number)
    if len(card_number_string) != 16:
        logger.info("Номер карты не верен")
        return "Номер карты неверен"
    mask_card_number = card_number_string[:6] + "******" + card_number_string[-4:]
    card_number_format = (
        mask_card_number[:4] + " " + mask_card_number[4:8] + " " + mask_card_number[8:12] + " " + mask_card_number[12:]
    )
    logger.info("Номер карты замаскирован")
    return card_number_format


def get_mask_account(account_number: int = 0) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info(f"маскировка номера карты: {account_number}")
    if account_number == 0:
        logger.info("Номер счета не введен")
        return "Номер счета не введен"
    account_number_string = str(account_number)
    if len(account_number_string) != 20:
        logger.info("Номер счета не верен")
        return "Номер счета неверен"
    account_number_format = "**" + account_number_string[-4:]
    logger.info("Номер счета замаскирован")
    return account_number_format
