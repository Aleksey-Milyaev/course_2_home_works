def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Функция принимающая список операций и возвращающая новый список операций со значением 'state'."""
    processed_operation_list = []
    for operation in operations:
        if operation["state"] == state:
            processed_operation_list.append(operation)

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
