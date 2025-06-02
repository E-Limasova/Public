def filter_by_currency(lst, s):
    """
    Генератор, который фильтрует список транзакций по коду валюты.

    Args:
        lst (list): Список словарей, содержащих информацию о транзакциях.
        s (str): Код валюты, по которому нужно отфильтровать транзакции (например, "USD").

    Yields:
        dict: Транзакции, у которых код валюты совпадает с заданным.
    """
    for i in lst:
        if i["operationAmount"]["currency"]["code"] == s:
            yield i


def transaction_descriptions(lst):
    """
    Генератор, который возвращает описания транзакций из списка.

    Args:
        lst (list): Список словарей, содержащих информацию о транзакциях.

    Yields:
        str: Описание каждой транзакции.
    """
    for i in lst:
        yield i["description"]


def card_number_generator(start, end):
    """
    Генерирует список отформатированных номеров карт от start до end включительно.

    Args:
        start (int): Начальный номер карты (16-значное число).
        end (int): Конечный номер карты (16-значное число).

    Returns:
        list: Список строк с номерами карт в формате 'XXXX XXXX XXXX XXXX'.
    """
    lst = ["{:016d}".format(i) for i in range(start, end + 1)]
    lst = [i[:4] + " " + i[4:8] + " " + i[8:12] + " " + i[12:] for i in lst]
    return lst
