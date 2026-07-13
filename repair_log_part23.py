# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: RepairLog
def print_table(data, headers):
    """Выводит список данных в компактной табличной форме."""
    widths = [len(str(h)) for h in headers]
    for row in data:
        for i, cell in enumerate(row):
            if len(str(cell)) > widths[i]:
                widths[i] = len(str(cell))

    lines = []
    sep = "─" * sum(widths) + "─"
    header_line = "│" + "│".join(f"{h:<{w}}" for h, w in zip(headers, widths)) + "│"
    lines.append(header_line)
    lines.append(sep)

    for row in data:
        line = "│" + "│".join(f"{str(cell):<{w}}" for cell, w in zip(row, widths)) + "│"
        lines.append(line)
    print("\n".join(lines))
