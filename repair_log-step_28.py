# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: RepairLog
def print_report(data: dict) -> None:
    items = data.get("items", [])
    if not items:
        print("Нет данных для отчёта.")
        return
    total_cost = sum(i["cost"] for i in items)
    avg_cost = total_cost / len(items) if items else 0
    categories = {}
    for i in items:
        cat = i.get("category", "other")
        categories[cat] = categories.get(cat, 0) + 1
    print(f"Всего записей: {len(items)}")
    print(f"Общая стоимость: {total_cost:.2f}")
    print(f"Средняя стоимость: {avg_cost:.2f}")
    if categories:
        print("Категории:")
        for cat, cnt in sorted(categories.items(), key=lambda x: -x[1]):
            print(f"  {cat}: {cnt} запись(ей)")
