# tests/test_widget.py

import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "card_input, expected_output",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 7922 8960 6361  ** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83 ** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30 ** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98 ** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92 ** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41 ** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_input, expected_output):
    assert mask_account_card(card_input) == expected_output


@pytest.mark.parametrize(
    "date_input, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-01T12:00:00.000000", "01.12.2023"),
        ("2022-05-15T08:30:00.123456", "15.05.2022"),
    ],
)
def test_get_data(date_input, expected_output):
    assert get_data(date_input) == expected_output
