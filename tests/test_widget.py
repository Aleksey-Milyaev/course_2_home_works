from src.widget import get_date, mask_account_card


def test_mask_account_card():
    """Тест функции обработки номера карты(счета)"""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Visa Platinum 70007922") == "Номер карты неверен"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 7365410843015") == "Номер счета неверен"
    assert mask_account_card() == "Данные не введены"


def test_get_date():
    """Тест функции принимающая строку с датой и возвращает дату в формате "ДД.ММ.ГГГГ"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-03-11") == "11.03.2024"
    assert get_date("") == "Дата передана некорректно"
    assert get_date("2024-03") == "Дата передана некорректно"
