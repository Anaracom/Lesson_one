# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: RepairLog
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "exported_at": datetime.now().isoformat(),
        "items": items,
        "settings": settings
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
