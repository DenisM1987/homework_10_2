def sample_transactions():
    return [
        {"state": "EXECUTED", "date": "2023-04-01T12:00:00"},
        {"state": "PENDING", "date": "2023-03-15T10:30:00"},
        {"state": "EXECUTED", "date": "2023-04-10T14:15:00"},
        {"state": "CANCELED", "date": "2023-02-20T09:45:00"},
    ]


def filter_by_state(sample_transactions):
    executed = filter_by_state(sample_transactions, "EXECUTED")
    assert len(executed) == 2
    assert all(t["state"] == "EXECUTED" for t in executed)


def sort_by_date(sample_transactions):
    sorted_asc = sort_by_date(sample_transactions,
                              ascending=True)
    dates = [t["date"] for t in sorted_asc]
    assert dates == ["2023-02-20T09:45:00", "2023-03-15T10:30:00",
                     "2023-04-01T12:00:00", "2023-04-10T14:15:00"]


def sort_by_date(sample_transactions):
    sorted_desc = sort_by_date(sample_transactions, ascending=False)
    dates = [t["date"]
             for t in sorted_desc]
    assert dates == ["2023-04-10T14:15:00", "2023-04-01T12:00:00",
                     "2023-03-15T10:30:00", "2023-02-20T09:45:00"]

