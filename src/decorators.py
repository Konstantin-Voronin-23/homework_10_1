from loguru import logger
from functools import wraps

def log(filename=None):
    if filename:
        logger.remove()
        logger.add(filename)
    def decotator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"{func.__name__} | {args} | {kwargs}")
                result = func(*args, **kwargs)
                logger.success(f"{func.__name__} | ok")
                return result
            except Exception as error:
                logger.error(f"{func.__name__} error: | {type(error).__name__} Inputs: {args} {kwargs}")
                raise
        return wrapper
    return decotator

@log("logs.txt")
def my_function(x, y):
    return x / y
