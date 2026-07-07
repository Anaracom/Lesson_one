# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: RepairLog
import json, os, glob

ARCHIVE_DIR = "archive"


def archive_entry(entry_path):
    """Перемещает завершённую запись из data/ в archive/."""
    if not entry_path.endswith(".json"):
        return False
    name = os.path.basename(entry_path).replace(".json", "")
    dest = os.path.join(ARCHIVE_DIR, f"{name}_archived.json")
    try:
        with open(entry_path) as src, open(dest, "w") as dst:
            json.dump(json.load(src), dst, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False


def archive_old_entries(data_dir="data"):
    """Архивирует все записи старше 90 дней или с статусом 'completed'."""
    from datetime import datetime, timedelta

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    archived = []
    now = datetime.now()
    cutoff = (now - timedelta(days=90)).date().isoformat()

    for path in glob.glob(os.path.join(data_dir, "*.json")):
        with open(path) as f:
            entry = json.load(f)
        status = entry.get("status", "")
        date_str = entry.get("date", "")
        if status == "completed" or (date_str and date_str <= cutoff):
            if archive_entry(path):
                archived.append(entry["id"])

    return archived


def get_archive_list(archive_dir=ARCHIVE_DIR):
    """Возвращает список всех заархивированных записей."""
    entries = []
    for path in glob.glob(os.path.join(archive_dir, "*.json")):
        with open(path) as f:
            entry = json.load(f)
        entry["_archived"] = True
        entries.append(entry)
    return sorted(entries, key=lambda e: e.get("date", ""))
