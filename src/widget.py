from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number_card: str = "") -> str:
    """Функция, которая умеет обрабатывать информацию о картах и о счетах"""
    if type_and_number_card == "":
        return "Данные не введены"
    type_and_number_list = type_and_number_card.split(" ")
    number = int(type_and_number_list[-1])
    if type_and_number_list[0].lower() == "счет":
        type_and_number_list[-1] = get_mask_account(number)
        if type_and_number_list[-1] == "Номер счета неверен":
            return "Номер счета неверен"
        if type_and_number_list[-1] == "Номер счета не введен":
            return "Номер счета не введен"
        mask_number = " ".join(type_and_number_list)
    else:
        type_and_number_list[-1] = get_mask_card_number(number)
        if type_and_number_list[-1] == "Номер карты неверен":
            return "Номер карты неверен"
        if type_and_number_list[-1] == "Номер карты не введен":
            return "Номер карты не введен"
        mask_number = " ".join(type_and_number_list)
    return mask_number


def get_date(date_: str) -> str:
    """Функция принимающая строку с датой и возвращает дату в формате "ДД.ММ.ГГГГ"""
    date_list = date_.split("T")[0].split("-")
    correct_date = ".".join(date_list[::-1])
    if len(correct_date) != 10:
        return "Дата передана некорректно"
    return correct_date
