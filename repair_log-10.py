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

# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: RepairLog
def export_to_json():
    import json
    data = {
        "items": items,
        "statistics": calculate_statistics() if statistics_enabled else None
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
