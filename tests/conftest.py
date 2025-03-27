import pytest

@pytest.fixture
def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"state": "PENDING", "date": "2023-01-03T00:00:00"},
        {"state": "EXECUTED", "date": "2023-01-02T00:00:00"},
        {"state": "CANCELED", "date": "2023-01-04T00:00:00"},
    ]
