def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2023-04-01T12:00:00"},
        {"state": "PENDING", "date": "2023-03-15T10:30:00"},
        {"state": "EXECUTED", "date": "2023-04-10T14:15:00"},
        {"state": "CANCELED", "date": "2023-02-20T09:45:00"},
    ]


def filter_by_state(transactions, state):
    """Фильтрует транзакции по состоянию."""
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions, reverse=False):
    """Сортирует транзакции по дате."""
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
