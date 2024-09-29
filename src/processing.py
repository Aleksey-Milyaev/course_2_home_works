from typing import Any


def filter_by_state(operations: Any = 0, state: str = "EXECUTED") -> str | list:
    """Функция принимающая список операций и возвращающая новый список операций со значением 'state'."""
    if operations == 0:
        return "Данные небыли переданы"
    processed_operation_list = []
    for operation in operations:
        try:
            if operation["state"] == state:
                processed_operation_list.append(operation)
        except KeyError:
            continue

    return processed_operation_list


def sort_by_date(operations: list, sort: bool = True) -> list:
    """Функция сортировки операций по дате, второй аргумент задает порядок сортировки, по умолчанию - убывание"""
    operation_sorted_list = []
    date_list = []
    for operation in operations:
        date_list.append(operation["date"][:10])
    date_list.sort(reverse=sort)
    for item in date_list:
        for operation in operations:
            if item in operation["date"]:
                operation_sorted_list.append(operation)
    return operation_sorted_list
