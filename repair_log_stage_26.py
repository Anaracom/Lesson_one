# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: RepairLog
def demo_mode():
    """Compact manual-testing entry point: prints 3 sample RepairLog records and exits."""
    from datetime import date, timedelta
    today = date.today()
    print("=== RepairLog Demo ===\n")

    def mk_report(title, item_type, cost, notes, duration_min):
        return {
            "title": title,
            "item_type": item_type,
            "cost": cost,
            "notes": notes,
            "duration_min": duration_min,
            "date": today - timedelta(days=[0, 5, 12][i % 3]),
        }

    reports = [
        mk_report("Phone screen crack", "Electronics", 45.0, "Replaced digitizer glass.", 60),
        mk_report("Car oil change", "Vehicle", 25.5, "Used synthetic 5W-30.", 45),
        mk_report("Fence repair", "Home", 150.0, "Patched rot on south gate.", 90),
    ]

    for r in reports:
        print(f"Date: {r['date']}")
        print(f"Title : {r['title']}")
        print(f"Type  : {r['item_type']}")
        print(f"Cost  : ${r['cost']:.2f}")
        print(f"Notes : {r['notes']}")
        print(f"Time  : {r['duration_min']} min")
        print("-" * 30)

    total = sum(r["cost"] for r in reports)
    avg   = total / len(reports)
    print(f"Total spend: ${total:.2f}")
    print(f"Avg per job : ${avg:.2f}")
    print("Demo complete.")
