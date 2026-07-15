# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: RepairLog
def show_entry(entry):
    """Compact one-entry view with details."""
    print(f"ID: {entry.id}")
    print(f"Item: {entry.item_name}")
    print(f"Date: {entry.date.strftime('%Y-%m-%d')}")
    if entry.cost is not None:
        print(f"Cost: ${entry.cost:.2f}")
    else:
        print("Cost: free")
    for detail in entry.details:
        print(f"- {detail.name} x{detail.quantity} @ ${detail.price:.2f} = ${detail.total:.2f}")
    if entry.notes:
        print(f"Notes: {entry.notes}")
