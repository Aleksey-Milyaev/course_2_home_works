import json
import logging
import os
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log"), "w")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_operations_list(path_to_json: str) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях."""
    try:
        with open(path_to_json, encoding="UTF8") as file:
            content = file.read()
            logger.info("Данные о транзакциях получены")
            return json.loads(content)
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
