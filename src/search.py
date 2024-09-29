import re
from typing import Any


def search_by_word(transactions: list, word: str) -> Any:
    """Функция сортировки транзакций по заданному слову"""
    try:
        pattern = re.compile(rf"{word}")
        found_transactions = []
        for transaction in transactions:
            for key, value in transaction.items():
                if pattern.search(str(key)) or pattern.search(str(value)):
                    found_transactions.append(transaction)
        if len(found_transactions) != 0:
            return found_transactions
        else:
            return []
    except Exception as ex:
        print(f"Ошибка {ex}")
