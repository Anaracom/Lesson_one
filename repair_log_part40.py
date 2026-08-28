# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: RepairLog
import argparse

def main():
    parser = argparse.ArgumentParser(description="RepairLog CLI")
    parser.add_argument("action", choices=["add", "list", "search"], help="Operation to perform")
    parser.add_argument("--item", "-i", help="Item name")
    parser.add_argument("--date", "-d", help="Date (YYYY-MM-DD)")
    parser.add_argument("--cost", "-c", type=float, help="Cost in rubles")
    parser.add_argument("--detail", help="Repair detail")
    parser.add_argument("--note", "-n", help="Note")
    parser.add_argument("--query", "-q", help="Search query")
    args = parser.parse_args()
    if args.action == "add":
        from repair_log import add_repair
        add_repair(item=args.item, date=args.date, cost=args.cost, detail=args.detail, note=args.note)
    elif args.action == "list":
        from repair_log import list_repair_logs
        list_repair_logs()
    elif args.action == "search":
        from repair_log import search_repair_logs
        search_repair_logs(query=args.query)
