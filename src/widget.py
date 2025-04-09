def mask_account_card(input_str: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа"""
    if "Счет" in input_str:
        # Обработка счета
        parts = input_str.split()
        account_number = parts[-1]
        return f"Счет **{account_number[-4:]}"
    else:
        # Обработка карты
        parts = input_str.split()
        card_number = parts[-1]
        masked_number = (f"{card_number[:4]} {card_number[4:6]}** **** "
                         f"{card_number[-4:]}")
        return f"{' '.join(parts[:-1])} {masked_number}"


def get_date(date_str: str) -> str:
    """Преобразует дату из формата ISO в DD.MM.YYYY"""
    from datetime import datetime
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
