import re

def validate_date(date_str: str) -> bool:
    """Проверка даты DD-MM-YYYY"""
    return bool(re.match(r"^\d{2}-\d{2}-\d{4}$", date_str))

def validate_amount(amount: str) -> bool:
    """Проверка пострадавших"""
    return bool(re.match(r"^\d+(\.\d{1,2})?$", amount))


