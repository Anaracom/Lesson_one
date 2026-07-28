# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: RepairLog
import json, os, sys

def get_log_file():
    path = "repairlog.json"
    if not os.path.exists(path):
        data = {"entries": []}
        with open(path, 'w') as f:
            json.dump(data, f)
    return path

def load_entries():
    try:
        with open(get_log_file(), 'r') as f:
            return json.load(f)
    except Exception:
        return {"entries": []}

def save_data(data):
    with open(get_log_file(), 'w') as f:
        json.dump(data, f)

def get_last_entry_id():
    data = load_entries()
    if not data["entries"]:
        return None
    last = data["entries"][-1]
    return last.get("id")

def undo_last_entry(entry):
    if entry.get("type") == "add":
        for i, e in enumerate(data["entries"]):
            if e["id"] == entry["id"]:
                data["entries"].pop(i)
                break
    elif entry.get("type") == "update":
        # update is stored as a new add with same id; we remove that last entry
        for i, e in enumerate(data["entries"]):
            if e["id"] == entry["id"]:
                data["entries"].pop(i)
                break
    elif entry.get("type") == "delete":
        # delete was recorded as an add with negative amount; remove it
        for i, e in enumerate(data["entries"]):
            if e["id"] == entry["id"]:
                data["entries"].pop(i)
                break

data = load_entries()
last_id = get_last_entry_id()
if last_id:
    undo_last_entry({"id": last_id})
save_data(data)
