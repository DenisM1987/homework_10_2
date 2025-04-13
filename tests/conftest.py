from datetime import datetime

import pytest


@pytest.fixture
def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2023-04-01T12:00:00"},
        {"state": "PENDING", "date": "2023-03-15T10:30:00"},
        {"state": "CANCELED", "date": "2023-02-20T09:45:00"},
    ]

from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        # ... (остальные транзакции из примера)
    ]
