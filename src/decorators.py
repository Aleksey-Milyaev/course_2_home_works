import os
from datetime import datetime
from typing import Any


def log(filename: str = "") -> Any:
    """Декоратор логирования начала и конца выполнения функции"""

    def decorator(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if filename:
                path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", f"{filename}")
                try:
                    start_time = datetime.now().time().strftime("%H:%M:%S")
                    result = func(*args, **kwargs)
                    finish_time = datetime.now().time().strftime("%H:%M:%S")
                    with open(path, "a", encoding="UTF8") as file:
                        file.write(
                            f"Функция: {func.__name__}\nначало работы функции: {start_time}\nРезультат:"
                            f" {result}\nКонец работы функции: {finish_time}\n"
                        )
                except Exception as e:
                    with open(path, "a", encoding="UTF8") as file:
                        file.write(f"Функция: {func.__name__}\nТип ошибки: {e}\nВходные данные: {args, kwargs}\n")
            else:
                try:
                    start_time = datetime.now().time().strftime("%H:%M:%S")
                    result = func(*args, **kwargs)
                    finish_time = datetime.now().time().strftime("%H:%M:%S")
                    print(
                        f"Функция: {func.__name__}\nначало работы функции: {start_time}\nРезультат:"
                        f" {result}\nКонец работы функции: {finish_time}\n"
                    )
                except Exception as e:
                    print(f"Функция: {func.__name__}\nТип ошибки: {e}\nВходные данные: {args, kwargs}\n")

        return wrapper

    return decorator
