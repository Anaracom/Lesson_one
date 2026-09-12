# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: RepairLog
def _format_entry(entry: RepairEntry) -> str:
    """Возвращает читаемое текстовое представление записи."""
    return (
        f"[{entry.id}] {entry.item}\n"
        f"  Дата: {entry.date}\n"
        f"  Затраты: {entry.cost} руб.\n"
        f"  Детали: {entry.details}\n"
        f"  Заметка: {entry.note}"
    )


def _format_summary() -> str:
    """Составляет итоговый отчёт по всем записям."""
    lines = ["=== RepairLog: Отчёт ==="]
    for e in RepairLog.entries:
        lines.append(_format_entry(e))
    total = sum(e.cost for e in RepairLog.entries)
    lines.append(f"\nИтого: {total} руб. за {len(RepairLog.entries)} записей.")
    return "\n".join(lines)


def print_report() -> None:
    """Выводит отчёт в консоль."""
    print(_format_summary())
