# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: RepairLog
def backup_data_file(data_file_path: str, backup_dir: str = "backups") -> str:
    """Сохраняет копию файла данных в папку backups с меткой даты-времени."""
    import os
    import shutil
    from datetime import datetime

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

    shutil.copy2(data_file_path, backup_path)
    print(f"Резервная копия сохранена: {backup_path}")
    return backup_path
