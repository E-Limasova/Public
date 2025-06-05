import functools
import logging


def get_logger(func_name, filename=None):
    """
    Создаёт и возвращает логгер для функции.

    Args:
        func_name (str): Имя функции, для которой создаётся логгер.
        filename (str, optional): Имя файла для записи логов. Если None — логирование в консоль.

    Returns:
        logging.Logger: Настроенный логгер.
    """
    logger = logging.getLogger(func_name)
    logger.setLevel(logging.INFO)

    # Избежать повторного добавления хендлеров
    if not logger.handlers:
        handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def log(filename=None):
    """
    Декоратор логирования вызовов функции.

    Args:
        filename (str, optional): Имя файла для записи логов. Если не задано — логируется в консоль.
    """
    def decorator(func):
        logger = get_logger(func.__name__, filename)

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
