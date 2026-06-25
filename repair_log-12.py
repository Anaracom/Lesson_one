# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: RepairLog
def load_from_json(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [RepairLogItem.from_dict(item) for item in data]
        elif isinstance(data, dict):
            return RepairLogItem.from_dict(data)
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла {filepath}: {e}")
        return []
