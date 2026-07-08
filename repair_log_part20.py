# === Stage 20: Добавь восстановление записей из архива ===
# Project: RepairLog
def restore_archive(file_path):
    """Восстанавливает записи из архива: парсит .txt/backup.json файлы."""
    if not os.path.exists(file_path):
        return 0, []
    
    ext = file_path.lower().rsplit('.', 1)[-1]
    records = []
    
    if ext in ('json', 'backup'):
        with open(file_path, 'r') as f:
            data = json.load(f)
        if isinstance(data, list):
            records = data
        elif isinstance(data, dict):
            records = data.get('records', [])
    else:
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    rec = json.loads(line.strip())
                    if isinstance(rec, dict) and 'id' in rec and 'item' in rec:
                        records.append(rec)
                except json.JSONDecodeError:
                    continue
    
    return len(records), records
