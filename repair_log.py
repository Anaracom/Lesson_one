# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: RepairLog
import datetime

def init_repair_log():
    """Инициализация базовой структуры данных RepairLog."""
    # Базовая структура записи о ремонте
    repair_entry = {
        "id": 1,
        "item_name": "Ноутбук",
        "date": datetime.date.today().isoformat(),
        "cost": 0.0,
        "details": "Замена термопасты и чистка от пыли.",
        "notes": "Клиент доволен результатом."
    }

    # Пример списка записей (в реальном проекте это будет список или БД)
    repair_log = [repair_entry]

    # Функция для добавления новой записи
    def add_repair(item_name, date_str, cost, details, notes):
        new_entry = {
            "id": len(repair_log) + 1,
            "item_name": item_name,
            "date": date_str,
            "cost": float(cost),
            "details": details,
            "notes": notes
        }
        repair_log.append(new_entry)
        return new_entry

    # Функция для вывода журнала
    def print_log():
        print(f"{'ID':<4} {'Дата':<12} {'Вещь':<15} {'Стоимость':<10} {'Детали'}")
        print("-" * 80)
        for entry in repair_log:
            print(f"{entry['id']:<4} {entry['date']:<12} {entry['item_name']:<15} {entry['cost']:<10.2f} {entry['details']}")

    # Точка входа: создание инициализации и демонстрация
    if not repair_log:
        print("Инициализация журнала ремонта...")
        add_repair("Стиральная машина", "2023-10-25", 1500.0, "Замена подшипника", "Работает тихо.")
        add_repair("Кофеварка", "2023-10-26", 450.0, "Чистка и замена фильтра", "Вкус кофе улучшился.")
    
    print_log()

if __name__ == "__main__":
    init_repair_log()
