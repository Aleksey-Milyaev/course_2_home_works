def get_mask_card_number(card_number: int = 0) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number == 0:
        return "Номер карты не введен"
    card_number_string = str(card_number)
    if len(card_number_string) != 16:
        return "Номер карты неверен"
    mask_card_number = card_number_string[:6] + "******" + card_number_string[-4:]
    card_number_format = (
        mask_card_number[:4] + " " + mask_card_number[4:8] + " " + mask_card_number[8:12] + " " + mask_card_number[12:]
    )

    return card_number_format


def get_mask_account(account_number: int = 0) -> str:
    """Функция маскировки номера банковского счета"""
    if account_number == 0:
        return "Номер счета не введен"
    account_number_string = str(account_number)
    if len(account_number_string) != 20:
        return "Номер счета неверен"
    account_number_format = "**" + account_number_string[-4:]

    return account_number_format

print(get_mask_card_number(7000792289606361))
print(get_mask_card_number(700079228960636157))
