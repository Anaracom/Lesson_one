# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: RepairLog
class RepairItem:
    def __init__(self, name, date_str, cost_str, details):
        self.name = name
        self.date = self._validate_date(date_str)
        self.cost = self._validate_cost(cost_str)
        self.details = details if isinstance(details, str) else str(details)

    @staticmethod
    def _validate_date(date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")

    @staticmethod
    def _validate_cost(cost_str):
        try:
            cost = float(cost_str)
            if cost < 0:
                raise ValueError("Затраты не могут быть отрицательными")
            return cost
        except ValueError:
            raise ValueError("Затраты должны быть числом")

def create_item(name, date_str, cost_str, details):
    try:
        item = RepairItem(name, date_str, cost_str, details)
        print(f"Создан новый журнал ремонта: {item.name} ({item.date}, {item.cost:.2f})")
        return item
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
        return None
