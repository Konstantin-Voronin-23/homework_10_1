from loguru import logger
from functools import wraps
from typing import TypeVar, Callable, Any, cast

F = TypeVar("F", bound=Callable[..., Any])

def log(filename: str | None=None) -> Callable[[F],F]:
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
def my_function(x: int, y: int) -> Any:
    """Функция принимает на вход числа x и y, и проводит с ними операцию деления, отправляя на выход результат или ошибку"""
    return x / y
