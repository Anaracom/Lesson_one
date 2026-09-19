# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: RepairLog
import json

class RepairLog:
    def __init__(self):
        self.entries = []
        self.favorites = set()
        self._save()

    def _save(self):
        with open('repair_log.json', 'w') as f:
            json.dump({'entries': self.entries, 'favorites': list(self.favorites)}, f)

    def add_entry(self, text, date, cost, details='', notes=''):
        entry = {'text': text, 'date': date, 'cost': float(cost), 'details': details, 'notes': notes}
        self.entries.append(entry)
        self._save()
        print(f"Added: {text} ({date}, {cost}₽)")
        return entry

    def toggle_favorite(self, index):
        if index < len(self.entries):
            if index in self.favorites:
                self.favorites.discard(index)
                print(f"Removed favorite: {self.entries[index]['text']}")
            else:
                self.favorites.add(index)
                print(f"Marked as favorite: {self.entries[index]['text']}")
            self._save()
        else:
            print("Invalid index")

    def show_all(self):
        if not self.entries:
            print("No entries yet. Add one with add_entry().")
            return
        print("\n=== All Entries ===")
        for i, e in enumerate(self.entries):
            fav = "★" if i in self.favorites else " "
            print(f"{fav} [{i}] {e['text']} | {e['date']} | {e['cost']:.2f}₽ | {e['details']} | {e['notes']}")

    def show_favorites(self):
        if not self.favorites:
            print("No favorites yet.")
            return
        print("\n=== Favorites ===")
        for i in sorted(self.favorites):
            if i < len(self.entries):
                e = self.entries[i]
                print(f"  [{i}] {e['text']} | {e['date']} | {e['cost']:.2f}₽ | {e['details']} | {e['notes']}")
