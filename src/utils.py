import json
from typing import Any


def get_operations_list(path_to_json: str) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях."""
    try:
        with open(path_to_json, encoding="UTF8") as file:
            content = file.read()
            return json.loads(content)
    except Exception:
        return []
