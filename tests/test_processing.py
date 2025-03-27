import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("PENDING", 1),
    ("CANCELED", 1),
    ("UNKNOWN", 0),
])
def test_filter_by_state(sample_transactions, state, expected_count):
    result = filter_by_state(sample_transactions, state)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(item["state"] == state for item in result)

@pytest.mark.parametrize("reverse, first_date", [
    (False, "2023-01-01"),
    (True, "2023-01-03"),
])
def test_sort_by_date(sample_transactions, reverse, first_date):
    sorted_data = sort_by_date(sample_transactions, reverse=reverse)
    assert sorted_data[0]["date"].startswith(first_date)
