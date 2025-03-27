def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры"""
    if not card_number or len(card_number) < 6:
        raise ValueError("Номер карты слишком короткий")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(account: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры"""
    if not account or len(account) < 4:
        raise ValueError("Номер счета слишком короткий")
    return f"**{account[-4:]}"
