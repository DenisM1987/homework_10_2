import pytest  # Добавьте этот импорт

from src.processing import \
    sample_transactions  # Импортируем функцию для тестов
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("PENDING", 1),
    ("CANCELED", 1),
    ("UNKNOWN", 0),
])
def test_filter_by_state(state, expected_count):
    transactions = sample_transactions()  # Используем вашу функцию
    result = filter_by_state(transactions, state)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(item["state"] == state for item in result)


@pytest.mark.parametrize("reverse, first_date", [
    (False, "2023-02-20"),  # Самая ранняя дата в ваших данных
    (True, "2023-04-10"),   # Самая поздняя дата в ваших данных
])
def test_sort_by_date(reverse, first_date):
    transactions = sample_transactions()  # Используем вашу функцию
    sorted_data = sort_by_date(transactions, reverse=reverse)
    assert sorted_data[0]["date"].startswith(first_date)
