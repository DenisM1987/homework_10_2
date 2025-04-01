def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры"""
    if not isinstance(card_number, str):
        raise TypeError("Номер карты должен быть строкой")
    if not card_number:
        raise ValueError("Номер карты не может быть пустым")
    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    if len(card_number) < 6:
        raise ValueError("Номер карты должен содержать минимум 6 цифр")

    visible_part = f"{card_number[:4]} {card_number[4:6]}"
    return f"{visible_part}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры"""
    if not isinstance(account, str):
        raise TypeError("Номер счета должен быть строкой")
    if not account:
        raise ValueError("Номер счета не может быть пустым")
    if not account.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")
    if len(account) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    return f"**{account[-4:]}"
