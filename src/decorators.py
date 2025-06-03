# decorators.py
from decorators import log

@log(filename="mylog.txt")
def divide(x, y):
    return x / y

import functools
import logging
from datetime import datetime


def log(filename=None):
    """
    Декоратор логирования вызовов функции.

    Args:
        filename (str, optional): Имя файла для записи логов. Если не задано — логируется в консоль.
    """
    def decorator(func):
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)

        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Убедиться, что не добавляется дубликат хендлеров
        if not logger.handlers:
            logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
        return wrapper
    return decorator
