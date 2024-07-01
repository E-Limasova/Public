# src/widget.py
def mask_account_card(data: str) -> str:
    if data.startswith("Счет"):
        # Маскировка счета
        return f"{data[:5]}**{data[-4:]}"
    else:
        # Маскировка карты
        parts = data.split()
        masked_number = f"{parts[-1][:4]} {parts[-1][4:6]} ** {parts[-1][-4:]}"
        return " ".join(parts[:-1]) + " " + masked_number


def get_data(date_str: str) -> str:
    from datetime import datetime
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime("%d.%m.%Y")
