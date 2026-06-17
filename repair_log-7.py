# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: RepairLog
def sort_records(records, key='date', reverse=False):
    if not records: return []
    order_map = {'date': lambda r: (r['created_at'] or '1970-01-01'), 
                 'priority': lambda r: (r.get('priority') or 3), 
                 'name': lambda r: (r['item_name'] or '')}
    key_func = order_map.get(key, order_map['date'])
    return sorted(records, key=key_func, reverse=reverse)
