def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_string = str(card_number)
    mask_card_number = card_number_string[:6] + "******" + card_number_string[-4:]
    card_number_format = (
        mask_card_number[:4] + " " + mask_card_number[4:8] + " " + mask_card_number[8:12] + " " + mask_card_number[12:]
    )

    return card_number_format


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_string = str(account_number)
    account_number_format = "**" + account_number_string[-4:]

    return account_number_format
