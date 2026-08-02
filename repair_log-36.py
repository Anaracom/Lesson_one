# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: RepairLog
def check_and_fix_data(records):
    """Проверка целостности записей: поиск дубликатов ID, пустых полей и корректность дат."""
    issues = []
    seen_ids = set()
    
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            records[i] = {}
        
        rid = rec.get('id') or rec.get('repair_id')
        if rid is None:
            issues.append(f"Запись {i}: отсутствует идентификатор")
            continue
        
        if rid in seen_ids:
            issues.append(f"Дубликат ID: {rid} (записи {seen_ids})")
        
        seen_ids.add(rid)
        
        for key in ['item_name', 'date', 'cost', 'note']:
            val = rec.get(key)
            if val is None or (isinstance(val, str) and not val.strip()):
                issues.append(f"Запись {i}: пустое поле '{key}'")
        
        date_str = rec.get('date')
        if date_str:
            try:
                datetime.strptime(str(date_str)[:10], '%Y-%m-%d')
            except ValueError:
                issues.append(f"Запись {i}: некорректная дата '{date_str}'")
    
    return records, issues

def repair_simple_problems(records):
    """Автоматический ремонт: заполнение пропущенных дат текущей, очистка пробелов в строках."""
    today = datetime.now().strftime('%Y-%m-%d')
    for rec in records:
        if not rec.get('date'):
            rec['date'] = today
        for key in ['item_name', 'note']:
            val = rec.get(key)
            if isinstance(val, str):
                rec[key] = val.replace(' ', '')
    return records

if __name__ == '__main__':
    test_data = [
        {'id': 1, 'item_name': 'Тостер', 'date': '2024-03-15', 'cost': 15.5},
        {'id': 2, 'item_name': 'Лампа', 'date': '2024-04-20', 'cost': 8.9},
        {'id': None, 'item_name': '', 'date': 'invalid-date', 'note': '   '},
    ]
    
    repaired = check_and_fix_data(test_data)
    print(f"Проблем: {repaired[1]}")
    
    fixed = repair_simple_problems(repaired[0])
    print("Исправлено:", fixed)
