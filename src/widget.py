import pytest
from widget import mask_account_card, get_date

@pytest.mark.parametrize("input_str, expected", [
    ("Счет 12345678", "Счет **5678"),
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("MasterCard 1234567812345678", "MasterCard 1234 5678 **** 5678"),
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2023-04-01T12:00:00", "01.04.2023"),
    ("2022-12-31T23:59:59", "31.12.2022"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
