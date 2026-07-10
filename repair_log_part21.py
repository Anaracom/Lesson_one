# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: RepairLog
class RepairReminder:
    def __init__(self, item_name, due_date, notes=""):
        self.item_name = item_name
        self.due_date = due_date  # YYYY-MM-DD string
        self.notes = notes
        self.completed = False

    @property
    def is_overdue(self):
        from datetime import date as _date
        today = _date.today()
        due = _date.fromisoformat(self.due_date)
        return due < today and not self.completed

    def mark_done(self):
        if self.is_overdue:
            print(f"⚠️  Reminder for '{self.item_name}' was overdue!")
        self.completed = True

    def __repr__(self):
        status = "✅ done" if self.completed else ("🔴 overdue" if self.is_overdue else "⏳ pending")
        return f"<RepairReminder {status} | {self.due_date}>"
