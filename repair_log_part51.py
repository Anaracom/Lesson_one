# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: RepairLog
class ChangeLog:
    def __init__(self):
        self.entries = []

    def log(self, action, item_id=None, details=None):
        from datetime import datetime
        entry = {
            "time": datetime.now().isoformat(),
            "action": action,
            "item_id": item_id,
            "details": details or ""
        }
        self.entries.append(entry)
        return entry

    def get_history(self, limit=10):
        return self.entries[-limit:]

    def __str__(self):
        lines = ["=== Изменения журнала ==="]
        for e in self.entries[-5:]:
            lines.append(f"[{e['time']}] {e['action']}")
            if e['item_id']:
                lines.append(f"  ID: {e['item_id']}")
            if e['details']:
                lines.append(f"  Детали: {e['details']}")
        return "\n".join(lines)
