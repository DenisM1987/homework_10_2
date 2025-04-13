import pytest

from fixtures.test_data import transactions
from src.generators import (card_number_generator,
                                       filter_by_currency,
                                       transaction_descriptions)


@pytest.mark.parametrize("currency,expected_count",
                         [("USD", 3), ("RUB", 2), ("EUR", 0)])
def test_filter_by_currency(currency, expected_count):
    filtered = filter_by_currency(transactions, currency)
    assert len(list(filtered)) == expected_count


def test_filter_by_currency_empty():
    assert len(list(filter_by_currency([],
                                       "USD"))) == 0


@pytest.mark.parametrize(
    "index,expected",
    [
        (0, "Перевод организации"),
        (1, "Перевод со счета на счет"),
        (3, "Перевод с карты на карту"),
    ],
)
def test_transaction_descriptions(index, expected):
    gen = transaction_descriptions(transactions)
    for _ in range(index):
        next(gen)
    assert next(gen) == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002",
                "0000 0000 0000 0003"]),
        (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
    ],
)
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected
