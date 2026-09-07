# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: RepairLog
MIGRATION_VERSION = 46

def migrate_to_version_46(records, output):
    """Adds a `summary` field to each record: total cost and count of parts used."""
    for rec in records:
        rec["summary"] = {
            "total_cost": rec.get("cost", 0),
            "parts_count": len(rec.get("parts", [])),
        }
    output["migration_version"] = MIGRATION_VERSION
    output["records"] = records
    return output
