import os
from typing import Any


def log(filename: str = "") -> Any:
    """Декоратор логирования начала и конца выполнения функции"""

    def decorator(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if filename:
                path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", f"{filename}")
                try:
                    func(*args, **kwargs)
                    with open(path, "a", encoding="UTF8") as file:
                        file.write(f"{func.__name__} ok\n")
                except Exception as e:
                    with open(path, "a", encoding="UTF8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs:{args, kwargs}\n")
            else:
                try:
                    func(*args, **kwargs)
                    print(f"{func.__name__} ok\n")
                except Exception as e:
                    print(f"{func.__name__} error: {e}. Inputs:{args, kwargs}\n")

        return wrapper

    return decorator
