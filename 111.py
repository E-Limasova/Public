def get_mask_card_number(card_number: str) -> str:
    # Проверяем, что card_number состоит только из цифр и не является пустой строкой
    if not card_number.isdigit() or len(card_number) < 6:
        raise ValueError("Некорректный номер карты")

    masked = card_number[:6] + " " + "** **" + " " + card_number[-4:]
    return masked


def get_mask_account(account_number: str) -> str:
    # Проверяем, что account_number состоит только из цифр и не является пустой строкой
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Некорректный номер счета")

    masked = "**" + account_number[-4:]
    return masked
