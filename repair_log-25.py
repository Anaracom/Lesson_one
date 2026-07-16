# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: RepairLog
def validate_date(date_str):
    """Validates date string in YYYY-MM-DD format and returns a tuple (year, month, day) or raises ValueError."""
    if not isinstance(date_str, str) or len(date_str) != 10:
        raise ValueError(f"Некорректный формат даты: '{date_str}'. Ожидается YYYY-MM-DD.")
    
    parts = date_str.split('-')
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    
    if not (1 <= year <= 9999):
        raise ValueError(f"Некорректный год: {year}. Ожидаемый диапазон: 1-9999.")
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days[1] = 29
    
    if not (1 <= month <= 12) or not (1 <= day <= month_days[month - 1]):
        raise ValueError(f"Некорректная дата: '{date_str}'. Проверьте месяц и день.")
    
    return (year, month, day)
