
list_of_dict = [
    {"id": 41428829, "state": "ИСПОЛНЕНО", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "ИСПОЛНЕНО", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "ОТМЕНЕНО", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "ОТМЕНЕНО", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(input_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    # Используем новую переменную внутри функции
    filtered_list = [d for d in input_list if d.get("state") == state]
    return filtered_list


# Вызываем функцию и сохраняем результат в глобальную переменную
list_of_dict = filter_by_state(list_of_dict)
print(list_of_dict)


def filter_by_state(input_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    # Используем новую переменную внутри функции
    filtered_list = [d for d in input_list if d.get("state") == state]
    return filtered_list


# Вызываем функцию и сохраняем результат в глобальную переменную
list_of_dict = filter_by_state(list_of_dict)
print(list_of_dict)


def sort_by_date(data, order='desc'):
    """
    Сортирует список словарей по полю 'date'.
    data: Список словарей.
    order: Порядок сортировки ('asc' или 'desc', по умолчанию 'desc').
    :return: Отсортированный список словарей.
    """
    if order not in ['asc', 'desc']:
        raise ValueError("Неверный параметр 'order'. Должен быть 'asc' или 'desc'.")

    # Используем встроенную функцию sorted для сортировки списка словарей
    return sorted(data, key=lambda x: x['date'], reverse=(order == 'desc'))


# Пример использования функции
operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

# Сортировка по убыванию даты
sorted_operations = sort_by_date(operations)
print(sorted_operations)