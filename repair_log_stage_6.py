# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: RepairLog
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for item in records:
        if status and item['status'] != status: continue
        if category and item.get('category') != category: continue
        if tags:
            item_tags = set(item.get('tags', [])).union(set(item.get('extra_tags', [])))
            if not any(t in item_tags for t in tags): continue
        filtered.append(item)
    return filtered
