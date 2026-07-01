# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: RepairLog
def get_monthly_stats(records):
    from collections import defaultdict
    stats = defaultdict(lambda: {'count': 0, 'total_cost': 0})
    for r in records:
        if isinstance(r['date'], str) and len(r['date']) == 10:
            try:
                date_obj = datetime.strptime(r['date'], '%Y-%m-%d')
                key = f"{date_obj.year}-{date_obj.month:02d}"
                stats[key]['count'] += 1
                if r.get('cost', 0):
                    stats[key]['total_cost'] += float(r['cost'])
            except ValueError:
                pass
    return {k: {'count': v['count'], 'avg_cost': round(v['total_cost']/v['count'], 2) if v['count'] else 0} for k, v in sorted(stats.items())}
