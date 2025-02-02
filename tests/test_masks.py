# tests/test_masks.py

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "123456 ** ** 3456"
    assert get_mask_card_number("7000792289606361") == "700079 ** ** 6361"
    with pytest.raises(ValueError):
        get_mask_card_number("12345")


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    with pytest.raises(ValueError):
        get_mask_account("123")
