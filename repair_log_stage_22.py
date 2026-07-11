# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: RepairLog
def check_overdue_reminders():
    now = datetime.now().date()
    overdue = []
    for item in items:
        if item.get('reminder_date') and item['reminder_date'] < now:
            overdue.append(item)
    return overdue
