import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_str, expected", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("Счет 123456789012", "Счет **9012"),
    ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
    ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2023-04-01T12:00:00", "01.04.2023"),
    ("2022-12-31T23:59:59", "31.12.2022"),
    ("2021-01-01T00:00:00", "01.01.2021"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
