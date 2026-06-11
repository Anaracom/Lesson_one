# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: RepairLog
import json
from datetime import datetime

def init_storage():
    try:
        with open("repair_log.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"items": [], "last_id": 0}

def save_storage(data):
    with open("repair_log.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_record(item_name, cost, details, notes=None):
    storage = init_storage()
    record_id = storage["last_id"] + 1
    record = {
        "id": record_id,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "item_name": item_name,
        "cost": cost,
        "details": details,
        "notes": notes or ""
    }
    storage["items"].append(record)
    storage["last_id"] = record_id
    save_storage(storage)
    return record
