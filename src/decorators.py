from functools import wraps
from typing import Any, Callable, TypeVar, cast

from loguru import logger

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: str | None = None) -> Callable[[F], F]:
    """Декоратор, принимает на вход необязательный параметр, filename который определяет куда будут записываться
    логи отработку функции, если он указан то логи будут записываться в указанный в данном параметре файл
    если данный файл не указан логи будет выводиться в консоль.
    Выводит логи о дате и времени начало операции, конце операции, результате и ошибках если такие есть"""
    if filename:
        logger.remove()
        logger.add(filename)

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """"""
            try:
                logger.info(f"{func.__name__} | {args} | {kwargs}")
                result = func(*args, **kwargs)
                logger.success(f"{func.__name__} | ok")
                return result
            except Exception as error:
                logger.error(f"{func.__name__} error: | {type(error).__name__} Inputs: {args} {kwargs}")
                raise
        return cast(F, wrapper)
    return decorator


@log("logs.txt")
def number_divide(x: int, y: int) -> float:
    """Функция принимает на вход числа x и y, и проводит с ними операцию деления,
     отправляя на выход результат или ошибку"""
    return x / y
