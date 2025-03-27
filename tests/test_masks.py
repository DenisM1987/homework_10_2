import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("123456", "1234 56** **** 3456"),  # Граничный случай
    ("123456789012", "1234 56** **** 9012"),  # Нестандартная длина
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account, expected", [
    ("12345678", "**5678"),
    ("1234", "**1234"),  # Граничный случай
    ("1234567890", "**7890"),  # Длинный номер
])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected

def test_get_mask_account_empty():
    with pytest.raises(ValueError):
        get_mask_account("")
