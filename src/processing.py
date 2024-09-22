def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Функция принимающая список операций и возвращающая новый список операций со значением 'state'."""
    processed_operation_list = []
    for operation in operations:
        if operation["state"] == state:
            processed_operation_list.append(operation)

    return processed_operation_list
