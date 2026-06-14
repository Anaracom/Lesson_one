# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: RepairLog
def delete_record(record_id):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    del records[record_id]
    print(f"Запись с ID {record_id} успешно удалена.")
    return True

def get_record_by_id(record_id):
    if record_id not in records:
        raise ValueError(f"Запись с ID {record_id} не найдена")
    return records[record_id]
