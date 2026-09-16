# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: RepairLog
def export_report_as_text(db, items, expenses, repairs, notes):
    """Export a compact text report from the RepairLog database."""
    lines = []
    lines.append("RepairLog Report")
    lines.append("=" * 20)
    lines.append(f"Items: {len(items)}, Expenses: {len(expenses)}, Repairs: {len(repairs)}, Notes: {len(notes)}")
    lines.append("")
    for item in items:
        lines.append(f"Item: {item['name']}")
        lines.append(f"  Date: {item['date']}")
        lines.append(f"  Cost: {item['cost']}")
        lines.append(f"  Details: {item['details']}")
        lines.append(f"  Notes: {item['notes']}")
        lines.append("")
    for repair in repairs:
        lines.append(f"Repair: {repair['description']}")
        lines.append(f"  Date: {repair['date']}")
        lines.append(f"  Cost: {repair['cost']}")
        lines.append(f"  Details: {repair['details']}")
        lines.append(f"  Notes: {repair['notes']}")
        lines.append("")
    for expense in expenses:
        lines.append(f"Expense: {expense['description']}")
        lines.append(f"  Date: {expense['date']}")
        lines.append(f"  Cost: {expense['cost']}")
        lines.append(f"  Details: {expense['details']}")
        lines.append(f"  Notes: {expense['notes']}")
        lines.append("")
    for note in notes:
        lines.append(f"Note: {note['text']}")
        lines.append(f"  Date: {note['date']}")
        lines.append(f"  Details: {note['details']}")
        lines.append(f"  Notes: {note['notes']}")
        lines.append("")
    return "\n".join(lines)
