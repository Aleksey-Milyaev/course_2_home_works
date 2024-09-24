import random


def filter_by_currency(transaction: list, currency: str) -> object:
    """Функция, возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    filter_transactions = filter(lambda y: y["operationAmount"]["currency"]["code"] == currency, transaction)
    return filter_transactions


def transaction_descriptions(transactions: list) -> object:
    """Функция генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по
    очереди."""
    description = (transaction["description"] for transaction in transactions)
    description_list = list(description)
    count = -1
    while True:
        count += 1
        yield description_list[count]


def card_number_generator(start: int = 1, stop: int = 9999_9999_9999_9999) -> object:
    """Функция генератор номера банковской карты"""
    while True:
        number_card = str(random.randint(start, stop))
        formated_number_card = f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"
        if len(number_card) < 16:
            zero = 16 - len(number_card)
            number_card = "0" * zero + number_card
            formated_number_card = f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"
            yield formated_number_card
        yield formated_number_card
