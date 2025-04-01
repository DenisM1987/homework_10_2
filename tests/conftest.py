from datetime import datetime

import pytest


@pytest.fixture
def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2023-04-01T12:00:00"},
        {"state": "PENDING", "date": "2023-03-15T10:30:00"},
        {"state": "CANCELED", "date": "2023-02-20T09:45:00"},
    ]
