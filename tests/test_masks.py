import pytest

from src.masks import (
    get_mask_account,
    get_mask_card_number,
)


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "123456 ** ** 3456"),
        ("7000792289606361", "700079 ** ** 6361"),
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "12345",
        "",
        "abc1234567890",
    ],
)
def test_get_mask_card_number_invalid(invalid_card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("123456789", "**6789"),
    ],
)
def test_get_mask_account_valid(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "123",
        "",
        "abc12345",
    ],
)
def test_get_mask_account_invalid(invalid_account_number):
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_number)
