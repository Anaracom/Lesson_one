# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: RepairLog
def _split_entry(text, max_len=50, sep="..."):
    """Разбивает длинный текст на строки по max_len символов с обрезкой."""
    if len(text) <= max_len:
        return text
    return text[:max_len] + sep


def _format_entry(entry):
    """Форматирует запись в строку для вывода в терминал."""
    lines = []
    for field, value in entry.items():
        if field == "notes":
            lines.append(f"{field}: {_split_entry(value)}")
        elif field == "details":
            if isinstance(value, list):
                for detail in value:
                    lines.append(f"  - {_split_entry(detail)}")
            else:
                lines.append(f"{field}: {_split_entry(value)}")
        else:
            lines.append(f"{field}: {_split_entry(value)}")
    return "\n".join(lines)


def _parse_entry(text):
    """Парсит строку из терминала обратно в словарь."""
    import re
    entry = {}
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        match = re.match(r"(\w+):\s*(.*)", line)
        if match:
            key, value = match.group(1), match.group(2)
            entry[key] = value
    return entry
