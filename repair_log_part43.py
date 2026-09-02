# === Stage 43: Добавь пагинацию длинных списков ===
# Project: RepairLog
def paginate(items, page_size=10):
    pages = []
    for i in range(0, len(items), page_size):
        pages.append(items[i:i+page_size])
    return pages

page, page_size = 0, 10
all_pages = paginate(all_repairs, page_size)
current_page = all_pages[page]
for idx, repair in enumerate(current_page):
    print(f"[{idx+1}] {repair.name} | Дата: {repair.date} | Затраты: {repair.cost:.2f}")

next_page = page + 1
if next_page < len(all_pages):
    print(f"\nДалее [{next_page+1}]: {all_pages[next_page][0].name}")
else:
    print("\nЭто последняя страница.")
