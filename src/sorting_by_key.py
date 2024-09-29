from collections import Counter
from typing import Any


def sorting_by_key(transactions: list, description: list) -> Any:
    """Функция сортировки транзакций по ключу 'description'."""
    try:

        description = [word.lower() for word in description]
        description_list = []
        for transaction in transactions:
            try:
                if transaction["description"].lower() in description:
                    description_list.append(transaction["description"])
            except KeyError:
                continue
        counted_description = Counter(description_list)
        return counted_description
    except Exception as es:
        print(f"Ошибка {es}")
