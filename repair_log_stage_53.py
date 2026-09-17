# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: RepairLog
def import_from_text(filename):
    records = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('#') or line.startswith('//'):
            i += 1
            continue
        if line.startswith('---'):
            i += 1
            continue
        parts = line.split(';', 5)
        if len(parts) < 5:
            i += 1
            continue
        item, date, cost, detail, note = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip()
        try:
            cost = float(cost)
        except ValueError:
            cost = 0.0
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            date = datetime.now().date()
        records.append({'item': item, 'date': date, 'cost': cost, 'detail': detail, 'note': note})
        i += 1
    return records
