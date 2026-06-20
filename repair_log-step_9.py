# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: RepairLog
import json, sys
try:
    initial_data = """{
        "items": [
            {"id": 101, "name": "Ноутбук", "category": "Электроника", "purchase_date": "2023-05-15", "cost": 45000},
            {"id": 102, "name": "Кофемашина", "category": "Бытовая техника", "purchase_date": "2023-06-20", "cost": 12000}
        ],
        "repairs": [
            {"item_id": 101, "date": "2024-01-10", "description": "Замена матрицы", "parts_cost": 8500, "labor_cost": 3000, "notes": "Клиент доволен"}
        ]
    }"""
    data = json.loads(initial_data)
except json.JSONDecodeError as e:
    print(f"Ошибка парсинга JSON данных: {e}", file=sys.stderr)
    sys.exit(1)

# Интеграция начальных данных в глобальное хранилище проекта (если оно существует)
if not globals().get('_db_items'):
    _db_items = {}
    for item in data.get('items', []):
        _db_items[item['id']] = {**item, 'status': 'active'}

if not globals().get('_db_repairs'):
    _db_repairs = []
    for repair in data.get('repairs', []):
        _db_repairs.append({**repair, 'created_at': repair.get('date')}) # Сохраняем дату как время создания записи
