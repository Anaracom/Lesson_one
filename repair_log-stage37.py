# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: RepairLog
import unittest


class TestRepairLog(unittest.TestCase):
    def setUp(self):
        from repair_log import RepairItem, RepairEntry, RepairLog
        self.log = RepairLog()

    def test_add_item_then_entry(self):
        item = RepairItem("phone", 150)
        entry = RepairEntry("screen_repair", "2024-06-01", 80, "replaced screen")
        self.log.add_item(item)
        self.log.add_entry(entry)

        entries = list(self.log.entries.values())
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].item_name, "phone")
        self.assertEqual(entries[0].detail, "replaced screen")
        self.assertGreaterEqual(
            sum(e.cost for e in entries), item.base_cost - entry.cost
        )

    def test_total_cost(self):
        item = RepairItem("laptop", 1200)
        for d in ["battery", "keyboard"]:
            entry = RepairEntry(d, "2024-05-10", 60, f"replaced {d}")
            self.log.add_item(item)
            self.log.add_entry(entry)

        total = sum(e.cost for e in list(self.log.entries.values()))
        self.assertEqual(total, 120)


if __name__ == "__main__":
    unittest.main()
