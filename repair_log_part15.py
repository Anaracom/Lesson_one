# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: RepairLog
def calculate_weekly_stats(records):
    from datetime import date, timedelta
    if not records: return {}
    dates = {r['date'] for r in records}
    week_start = min(dates) - timedelta(days=week_start.weekday())
    weekly_data = {}
    current_date = week_start + timedelta(weeks=1)
    while True:
        week_end = current_date + timedelta(days=6)
        week_records = [r for r in records if week_start <= date.fromtimestamp(r['date']) < week_end]
        total_cost = sum(float(r.get('cost', 0)) for r in week_records)
        count = len(week_records)
        weekly_data[current_date.isoformat()] = {'count': count, 'total_cost': round(total_cost, 2)} if count else None
        current_date += timedelta(days=7)
        if not any(dates and d >= current_date for d in dates): break
    return {k: v for k, v in weekly_data.items() if v is not None}
