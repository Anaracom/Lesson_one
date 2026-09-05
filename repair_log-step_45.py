# === Stage 45: Добавь восстановление из резервной копии ===
# Project: RepairLog
def restore_from_backup(backup_path: str, target_path: str) -> bool:
    """Восстановить журнал из резервной копии в целевой файл.
    Возвращает True при успехе, False при ошибке.
    """
    import json
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False
