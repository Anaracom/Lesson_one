# === Stage 17: Добавь группировку записей по категориям ===
# Project: RepairLog
from collections import defaultdict

def group_by_category(records):
    grouped = defaultdict(list)
    for record in records:
        cat = record.get('category', 'Other') or 'Other'
        grouped[cat].append(record)
    return dict(sorted(grouped.items()))
