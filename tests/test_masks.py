import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("123456789012", "1234 56** **** 9012"),
    ("12345678901234567890", "1234 56** **** 7890"),
    ("123456", "1234 56** **** 3456"),
    ("0000000000000000", "0000 00** **** 0000"),
    ("9999999999999999", "9999 99** **** 9999"),
])
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_card, expected_error", [
    ("", "Номер карты не может быть пустым"),
    ("12345", "Номер карты должен содержать минимум 6 цифр"),
    ("1234abcd56789012", "Номер карты должен содержать только цифры"),
    ("1234 5678 9012 3456", 'Номер карты должен содержать только цифры'),
    ("1234-5678-9012-3456", "Номер карты должен содержать только цифры"),
    (None, "Номер карты должен быть строкой"),
    (True, "Номер карты должен быть строкой"),
    ([], "Номер карты должен быть строкой"),
    ({}, "Номер карты должен быть строкой"),
    (3.14, "Номер карты должен быть строкой"),
])
def test_get_mask_card_number_invalid(invalid_card, expected_error):
    with pytest.raises((ValueError, TypeError)) as exc_info:
        get_mask_card_number(invalid_card)
    assert str(exc_info.value) == expected_error


# Тесты для get_mask_account
@pytest.mark.parametrize("account, expected", [
    ("12345678", "**5678"),
    ("1234", "**1234"),
    ("1234567890", "**7890"),
    ("00000000", "**0000"),
    ("99999999", "**9999"),
    ("10000004", "**0004"),
])
def test_get_mask_account_valid(account, expected):
    assert get_mask_account(account) == expected


@pytest.mark.parametrize("invalid_account, expected_error", [
    ("", "Номер счета не может быть пустым"),
    ("123", "Номер счета должен содержать минимум 4 цифры"),
    ("abcd5678", "Номер счета должен содержать только цифры"),
    ("12 345678", "Номер счета должен содержать только цифры"),
    ("1234-5678", "Номер счета должен содержать только цифры"),
    (None, "Номер счета должен быть строкой"),
    (False, "Номер счета должен быть строкой"),
    ([], "Номер счета должен быть строкой"),
    ({}, "Номер счета должен быть строкой"),
    (5.67, "Номер счета должен быть строкой"),
])
def test_get_mask_account_invalid(invalid_account, expected_error):
    with pytest.raises((ValueError, TypeError)) as exc_info:
        get_mask_account(invalid_account)
    assert str(exc_info.value) == expected_error


# Дополнительные тесты для полного покрытия
def test_get_mask_card_number_immutability():
    original = "1234567890123456"
    masked = get_mask_card_number(original)
    assert original == "1234567890123456"
    assert original is not masked


def test_get_mask_account_immutability():
    original = "12345678"
    masked = get_mask_account(original)
    assert original == "12345678"
    assert original is not masked


def test_get_mask_card_number_return_type():
    result = get_mask_card_number("1234567890123456")
    assert isinstance(result, str)


def test_get_mask_account_return_type():
    result = get_mask_account("12345678")
    assert isinstance(result, str)


def test_get_mask_card_number_exact_min_length():
    result = get_mask_card_number("123456")
    assert result == "1234 56** **** 3456"


def test_get_mask_account_exact_min_length():
    result = get_mask_account("1234")
    assert result == "**1234"


def test_get_mask_card_number_with_whitespace():
    with pytest.raises(ValueError):
        get_mask_card_number(" 1234567890123456 ")


def test_get_mask_account_with_whitespace():
    with pytest.raises(ValueError):
        get_mask_account(" 12345678 ")


def test_get_mask_card_number_special_chars():
    with pytest.raises(ValueError):
        get_mask_card_number("1234-5678-9012-3456")


def test_get_mask_account_special_chars():
    with pytest.raises(ValueError):
        get_mask_account("1234-5678")


def test_get_mask_card_number_with_letters():
    with pytest.raises(ValueError):
        get_mask_card_number("1234abcd56789012")


def test_get_mask_account_with_letters():
    with pytest.raises(ValueError):
        get_mask_account("abcd5678")


def test_get_mask_account_input_unchanged():
    original = "12345678"
    original_copy = original[:]
    _ = get_mask_account(original)
    assert original == original_copy


def test_get_mask_card_number_formatting():
    result = get_mask_card_number("1234567890123456")
    parts = result.split()
    assert len(parts) == 4
    assert parts[0] == "1234"
    assert parts[1] == "56**"
    assert parts[2] == "****"
    assert parts[3] == "3456"


@pytest.mark.parametrize("invalid_input", [
    b"1234567890123456",  # bytes
    bytearray(b"1234567890123456"),
    ("1" * 6,),  # tuple
    {"card": "1234567890123456"},  # dict
])
def test_get_mask_card_number_invalid_types(invalid_input):
    with pytest.raises(TypeError):
        get_mask_card_number(invalid_input)


def test_get_mask_card_number_exact_max_length():
    long_number = "1" * 20
    result = get_mask_card_number(long_number)
    assert result == "1111 11** **** 1111"
