from datetime import datetime
def mask_account_card(data: str) -> str:
    """
    Маскирует номер банковского счёта или карты в строке.

    Если строка начинается с "Счет", маскируется счёт:
        Пример: "Счет 40817810099910004312" → "Счет **4312"

    Иначе маскируется карта:
        Пример: "Visa Classic 1234567812345678" → "Visa Classic 1234 56 ** 5678"

    Args:
        data (str): Строка с типом и номером карты или счёта.

    Returns:
        str: Маскированная строка с картой или счётом.
    """
    if data.startswith("Счет"):
        return f"{data[:5]}**{data[-4:]}"
    else:
        parts = data.split()
        masked_number = f"{parts[-1][:4]} {parts[-1][4:6]} ** {parts[-1][-4:]}"
        return " ".join(parts[:-1]) + " " + masked_number


def get_data(date_str: str) -> str:
    """
    Преобразует дату из формата ISO 8601 в строку формата "ДД.ММ.ГГГГ".

    Пример:
        Вход: "2019-07-03T18:35:29.512364"
        Выход: "03.07.2019"

    Args:
        date_str (str): Строка даты в формате ISO 8601 (с миллисекундами).

    Returns:
        str: Строка даты в формате "день.месяц.год" (например, "03.07.2019").
    """
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime("%d.%m.%Y")
