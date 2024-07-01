# tests/test_widget.py

from src.widget import mask_account_card, get_data


def test_mask_account_card():
    # Пример для карты
    card_input = "Visa Platinum 7000 7922 8960 6361"
    card_output = mask_account_card(card_input)
    assert card_output == "Visa Platinum 7000 7922 8960 6361  ** 6361"

    # Пример для счета
    account_input = "Счет 73654108430135874305"
    account_output = mask_account_card(account_input)
    assert account_output == "Счет **4305"

    # Дополнительные примеры
    examples = [
        ("Maestro 1596837868705199", "Maestro 1596 83 ** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30 ** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98 ** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92 ** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41 ** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ]

    for input_str, expected_output in examples:
        assert mask_account_card(input_str) == expected_output


def test_get_data():
    date_input = "2024-03-11T02:26:18.671407"
    date_output = get_data(date_input)
    assert date_output == "11.03.2024"

    # Дополнительные примеры
    date_examples = [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-01T12:00:00.000000", "01.12.2023"),
        ("2022-05-15T08:30:00.123456", "15.05.2022"),
    ]

    for input_str, expected_output in date_examples:
        assert get_data(input_str) == expected_output


if __name__ == "__main__":
    test_mask_account_card()
    test_get_data()
    print("Все тесты пройдены успешно!")
