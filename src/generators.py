from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]],
                       currency_code: str) -> (
        Iterator)[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданному коду валюты.

    Args:
        transactions: Список транзакций (словарей).
        currency_code: Код валюты для фильтрации (например, "USD").

    Yields:
        Транзакции, где валюта операции соответствует currency_code.
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        transaction_currency = operation_amount.get("currency", {}).get("code")
        if transaction_currency == currency_code:
            yield transaction


def transaction_descriptions(transactions:
        List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    Args:
        transactions: Список транзакций (словарей).

    Yields:
        Описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне.

    Args:
        start: Начальный номер карты.
        end: Конечный номер карты (включительно).

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX".
    """

    for number in range(start, end + 1):
        yield (f"{number:016d}"[:4] + " " +
               f"{number:016d}"[4:8] + " " + f"{number:016d}"[
                          8:12] + " " + f"{number:016d}"[12:16])
