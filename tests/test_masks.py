import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number(70007922896063614356) == "Номер карты неверен"
    assert get_mask_card_number() == "Номер карты не введен"


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account(7000792289606361) == "Номер счета неверен"
    assert get_mask_account() == "Номер счета не введен"
