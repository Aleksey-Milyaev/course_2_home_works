from collections import defaultdict
from typing import Any


def sorting_by_key(transactions: list, description: list) -> Any:
    """Функция сортировки транзакций по ключу 'description'."""
    try:
        description = [word.lower() for word in description]
        sorting_dict: dict = defaultdict(dict)
        for transaction in transactions:
            try:
                if transaction["description"].lower() in description:
                    sorting_dict[transaction["description"]] = transaction
            except KeyError:
                continue
        return dict(sorting_dict)
    except Exception as es:
        print(f"Ошибка {es}")
