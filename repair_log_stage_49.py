# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: RepairLog
def self_check():
    """Финальная самопроверка: импортируем сущности и проверяем, что все таблицы/функции доступны."""
    from repairlog.models import Item, Repair, Note, Cost, Detail
    from repairlog.database import get_db
    from repairlog.ui import print_menu, run_app

    print("=" * 40)
    print("RepairLog — самопроверка")
    print("=" * 40)

    # 1. Модельные проверки
    assert hasattr(Item, "name")
    assert hasattr(Repair, "date")
    assert hasattr(Note, "text")
    assert hasattr(Cost, "amount")
    assert hasattr(Detail, "part")
    print("[OK] все модели определены")

    # 2. Проверка работы с БД (создаём тестовый ремонт, если БД пустая)
    db = get_db()
    if db.session.query(Item).count() == 0:
        test_item = Item(name="Ноутбук", owner="Тест")
        test_repair = Repair(item=test_item, date="2026-06-01", cost=1500.0)
        test_note = Note(repair=test_repair, text="Зарядка не держала")
        test_cost = Cost(repair=test_repair, amount=500.0)
        test_detail = Detail(repair=test_repair, part="Зарядка", note="замена")
        db.session.add_all([test_item, test_repair, test_note, test_cost, test_detail])
        db.session.commit()
        print("[OK] тестовые данные записаны")

    # 3. Проверка выборки
    items = db.session.query(Item).all()
    assert len(items) == 1
    assert items[0].name == "Ноутбук"
    repairs = db.session.query(Repair).all()
    assert len(repairs) == 1
    assert repairs[0].cost == 1500.0
    print("[OK] выборка работает корректно")

    # 4. Проверка UI-функций (без запуска full UI, просто импорты)
    assert callable(print_menu)
    assert callable(run_app)
    print("[OK] UI-функции доступны")

    print("=" * 40)
    print("RepairLog готов к использованию!")
    print("=" * 40)
