# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: RepairLog
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    for key, value in updates.items():
        if key in ["id", "created_at"]:
            continue
        records[record_id][key] = value
    print(f"Запись #{record_id} обновлена успешно.")
    return True
