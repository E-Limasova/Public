def filter_by_state(input_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по заданному значению поля 'state'.

    Args:
        input_list (list[dict]): Список словарей, содержащих поле 'state'.
        state (str): Значение состояния, по которому фильтруются элементы (по умолчанию "EXECUTED").

    Returns:
        list[dict]: Список словарей, у которых значение поля 'state' соответствует заданному.
    """
    filtered_list = [d for d in input_list if d.get("state") == state]
    return filtered_list


def sort_by_date(data: list[dict], order: str = 'desc') -> list[dict]:
    """
    Сортирует список словарей по дате, указанной в поле 'date'.

    Args:
        data (list[dict]): Список словарей, каждый из которых содержит ключ 'date' в формате ISO 8601.
        order (str): Порядок сортировки: 'asc' — по возрастанию, 'desc' — по убыванию (по умолчанию 'desc').

    Returns:
        list[dict]: Список словарей, отсортированный по дате.

    Raises:
        ValueError: Если передан некорректный параметр 'order' (не 'asc' и не 'desc').
    """
    if order not in ['asc', 'desc']:
        raise ValueError("Неверный параметр 'order'. Должен быть 'asc' или 'desc'.")

    return sorted(data, key=lambda x: x['date'], reverse=(order == 'desc'))
