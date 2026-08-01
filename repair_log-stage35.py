# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: RepairLog
def get_next_action(item: dict) -> str:
    """Рекомендует следующее действие для вещи на основе её состояния."""
    status = item.get("status", "").lower()
    last_date = item.get("last_service_date")
    notes = item.get("notes", "")
    
    if not last_date:
        return "Запланировать первое обслуживание"
    
    try:
        from datetime import datetime, timedelta
        now = datetime.now()
        last = datetime.strptime(last_date[:10], "%Y-%m-%d")
        days_since = (now - last).days
        
        if status in ("needs_service", "damaged"):
            return "Провести ремонт и обновить статус"
        
        if status == "repaired":
            if days_since < 30:
                return "Оставить в текущем состоянии, проверять раз в месяц"
            elif days_since < 90:
                return "Запланировать профилактическое обслуживание через неделю"
            else:
                return "Провести полное техническое обслуживание"
        
        if status == "serviced":
            if days_since < 60:
                return "Оставить в текущем состоянии, проверять каждые 2 месяца"
            elif days_since < 180:
                return "Запланировать плановое ТО через месяц"
            else:
                return "Провести капитальное обслуживание или замену"
        
        if status == "discarded":
            return "Утилизировать и удалить запись из активного журнала"
        
    except Exception:
        return "Проверить данные о дате последнего обслуживания"
    
    return "Обновить статус на основе текущего состояния вещи"
