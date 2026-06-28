# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: RepairLog
def generate_summary():
    if not items: return print("Нет данных для сводки.")
    total_cost = sum(item.cost for item in items)
    today = datetime.date.today()
    active_items = [i for i in items if (today - i.created_at).days < 365]
    inactive_count = len(items) - len(active_items)
    print(f"\n=== Сводка RepairLog ===")
    print(f"Всего записей: {len(items)} | Активных (<1 год): {len(active_items)} | Архивных: {inactive_count}")
    print(f"Общие затраты: {total_cost:.2f} руб.")
    if active_items:
        avg_age = sum((today - i.created_at).days for i in active_items) / len(active_items)
        print(f"Ср. возраст активных вещей: {avg_age:.1f} дней")
    else:
        print("Активных записей нет.")
