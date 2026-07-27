# === Stage 32: Добавь журнал действий пользователя ===
# Project: RepairLog
class ActionLog:
    def __init__(self):
        self._actions = []

    def add(self, action_type, description, timestamp=None):
        if timestamp is None:
            import datetime as dt
            timestamp = dt.datetime.now()
        record = {
            'timestamp': timestamp,
            'action_type': action_type,
            'description': description,
        }
        self._actions.append(record)

    def get(self):
        return list(self._actions)

    @property
    def count(self):
        return len(self._actions)
