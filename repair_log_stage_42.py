# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: RepairLog
import sys

def _reset():
    sys.stdout.write("\033[0m")

def _bold(text):
    sys.stdout.write(f"\033[1m{text}\033[0m")

def _red(text):
    sys.stdout.write(f"\033[31m{text}\033[0m")

def _green(text):
    sys.stdout.write(f"\033[32m{text}\033[0m")

def _yellow(text):
    sys.stdout.write(f"\033[33m{text}\033[0m")

def _cyan(text):
    sys.stdout.write(f"\033[36m{text}\033[0m")

def _magenta(text):
    sys.stdout.write(f"\033[35m{text}\033[0m")

def _blue(text):
    sys.stdout.write(f"\033[34m{text}\033[0m")

def _white(text):
    sys.stdout.write(f"\033[37m{text}\033[0m")

def _dim(text):
    sys.stdout.write(f"\033[2m{text}\033[0m")

def _log_info(msg):
    _cyan(f"[INFO]  {msg}")

def _log_success(msg):
    _green(f"[SUCCESS] {msg}")

def _log_warning(msg):
    _yellow(f"[WARNING] {msg}")

def _log_error(msg):
    _red(f"[ERROR]  {msg}")

def _log_title(title):
    _bold(f"═══ {title} ═══")

def _log_sub(title):
    _bold(f"── {title} ──")

def _log_detail(label, value):
    _dim(f"  {label}:")
    _white(f"  {value}")

def _log_summary(title, data):
    _bold(f"\n  {title}:")
    for key, val in data.items():
        _dim(f"  - {key}:")
        _white(f"  - {val}")
