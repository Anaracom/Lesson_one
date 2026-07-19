# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: RepairLog
def reset_demo_data(db_path):
    """Заполнить БД тестовыми записями и сбросить все валидации."""
    demo = [
        ("Ремонт ноутбука", "2024-03-15", 500, ["Замена матрицы"], "Сломался при падении"),
        ("Мойка машины", "2024-04-01", 800, ["Химия", "Пеногенератор"], ""),
        ("Ремонт холодильника", "2024-05-10", 3200, ["Компрессор", "Трубки фреона"], "Не морозит"),
    ]
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for name, date, cost, detail, note in demo:
        c.execute("INSERT OR REPLACE INTO repairs (name, repair_date, cost, details, notes) VALUES (?, ?, ?, ?, ?)",
                   (name, date, cost, " | ".join(detail), note))
    conn.commit()
    conn.close()
