# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: RepairLog
def search_records(query, fields=None):
    if not query: return []
    if fields is None: fields = ['item', 'date_str', 'cost_str', 'notes']
    q_lower = query.lower()
    results = [r for r in records if any(q_lower in str(v).lower() for v in (r.get(f) or '')) for f in fields]
    return sorted(results, key=lambda x: x['date'], reverse=True)
