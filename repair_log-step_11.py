# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: RepairLog
import json, os

DATA_FILE = "repair_log.json"

def save_data(items):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[Ошибка сохранения] {e}")
        return False

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('items', [])
    except Exception:
        return []

if __name__ == "__main__":
    # Пример инициализации пустого файла при первом запуске
    if not os.path.exists(DATA_FILE):
        save_data({"items": [], "version": 1})
