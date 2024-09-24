import os
from datetime import datetime
from typing import Any

from src.decorators import log


@log(filename="testlog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


def test_log_complete() -> Any:
    """Тест декоратора логирования, вывод данных при выполненной функции"""
    my_function(1, 2)
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "testlog.txt")
    with open(path, encoding="utf8") as file:
        content = file.read()
    assert (
        content
        == f"""Функция: my_function
начало работы функции: {datetime.now().time().strftime("%H:%M:%S")}
Результат: 3
Конец работы функции: {datetime.now().time().strftime("%H:%M:%S")}
"""
    )


def test_log_argument_error() -> Any:
    """Тест декоратора логирования, вывод данных при отсутствии одного аргумента"""
    my_function(1)
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "testlog.txt")
    with open(path, encoding="utf8") as file:
        content = file.read()
    assert (
        content
        == """Функция: my_function
Тип ошибки: my_function() missing 1 required positional argument: 'y'
Входные данные: ((1,), {})
"""
    )


def test_log(capsys: Any) -> Any:
    """Тест декоратора логирования, вывод данных в терминал"""

    @log()
    def my_function_(a: int, b: int) -> int:
        return a + b

    my_function_(1, 2)
    capture = capsys.readouterr()
    assert (
        capture.out
        == f"""Функция: my_function_
начало работы функции: {datetime.now().time().strftime("%H:%M:%S")}
Результат: 3
Конец работы функции: {datetime.now().time().strftime("%H:%M:%S")}
\n"""
    )
