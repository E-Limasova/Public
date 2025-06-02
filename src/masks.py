def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.

    Пример:
        Вход: "1234567890123456"
        Выход: "123456 ** ** 3456"

    Args:
        card_number (str): Номер карты в виде строки, состоящей из цифр.

    Returns:
        str: Маскированный номер карты.

    Raises:
        ValueError: Если номер карты содержит недопустимые символы или слишком короткий.
    """
    if not card_number.isdigit() or len(card_number) < 6:
        raise ValueError("Некорректный номер карты")

    masked = card_number[:6] + " ** ** " + card_number[-4:]
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счёта, оставляя видимыми только последние 4 цифры.

    Пример:
        Вход: "40817810099910004312"
        Выход: "**4312"

    Args:
        account_number (str): Номер счёта в виде строки, состоящей из цифр.

    Returns:
        str: Маскированный номер счёта.

    Raises:
        ValueError: Если номер счёта содержит недопустимые символы или слишком короткий.
    """
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Некорректный номер счета")

    masked = "**" + account_number[-4:]
    return masked

