# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: RepairLog
def dry_run_mode():
    """Включает режим dry-run для операций изменения данных.
    В этом режиме все операции записываются в лог, но не применяются."""
    global dry_run_active
    dry_run_active = True
    print("Режим dry-run включен. Изменения не будут применены.")
    return dry_run_active

def execute_dry_run(operation, data=None):
    """Выполняет операцию в режиме dry-run и сохраняет результат в лог."""
    if not dry_run_active:
        print("Режим dry-run не активен.")
        return operation
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "operation": operation,
        "data": data,
        "executed": False
    }
    log_entries.append(log_entry)
    print(f"Сухо-запуск: {operation} (данные: {data})")
    return log_entry
