# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: RepairLog
def show_menu():
    while True:
        print("\n=== RepairLog Меню ===")
        print("1. Добавить запись о ремонте")
        print("2. Показать все записи")
        print("3. Поиск по названию вещи")
        print("4. Выход")
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == "1":
            item_name = input("Название вещи: ")
            date_str = input("Дата ремонта (ДД.ММ.ГГГГ): ")
            cost = float(input("Затраты (руб.): ")) or 0
            details = input("Детали/Нюансы: ") or "Нет"
            notes = input("Заметки: ") or "-"
            
            record = {
                "item": item_name,
                "date": date_str,
                "cost": cost,
                "details": details,
                "notes": notes
            }
            records.append(record)
            print(f"Запись '{item_name}' добавлена.")
        
        elif choice == "2":
            if not records:
                print("Список записей пуст.")
            else:
                for i, r in enumerate(records):
                    print(f"\n[{i+1}] {r['item']} | {r['date']} | {r['cost']:.2f} руб. | {r['details']}")
        
        elif choice == "3":
            search_term = input("Введите название вещи для поиска: ").lower()
            found = [r for r in records if search_term in r["item"].lower()]
            if not found:
                print("Ничего не найдено.")
            else:
                for i, r in enumerate(found):
                    print(f"\n[{i+1}] {r['item']} | {r['date']} | {r['cost']:.2f} руб. | {r['details']}")
        
        elif choice == "4":
            confirm = input("Вы уверены? (y/n): ").strip().lower()
            if confirm == 'y':
                print("До свидания!")
                break
        
        else:
            print("Некорректный выбор.")
