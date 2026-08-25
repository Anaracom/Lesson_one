# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: RepairLog
import unittest
from datetime import date, timedelta

class TestEdgeCases(unittest.TestCase):
    def test_zero_cost(self):
        log = RepairLog()
        log.add_entry("Телефон", date.today(), 0, "Замена батареи", "Батарея села")
        entries = log.get_entries()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].cost, 0)

    def test_negative_cost(self):
        log = RepairLog()
        log.add_entry("Ноут", date.today(), -50, "Обмен детали", "Деталь под замену")
        entries = log.get_entries()
        self.assertEqual(entries[0].cost, -50)

    def test_empty_description(self):
        log = RepairLog()
        log.add_entry("Стол", date.today(), 100, "", "Стол поправлен")
        entries = log.get_entries()
        self.assertEqual(entries[0].description, "")

    def test_many_details(self):
        log = RepairLog()
        log.add_entry("Телевизор", date.today(), 200, "Экран", "Экран треснул")
        log.add_entry("Телевизор", date.today(), 150, "Кабель", "Кабель порвался")
        log.add_entry("Телевизор", date.today(), 100, "Дистанция", "Дистанция сломалась")
        entries = log.get_entries()
        self.assertEqual(len(entries), 3)

    def test_many_notes(self):
        log = RepairLog()
        log.add_entry("Микроволновка", date.today(), 50, "Замена", "Замена лампы")
        log.add_entry("Микроволновка", date.today(), 50, "Замена", "Замена кнопки")
        log.add_entry("Микроволновка", date.today(), 50, "Замена", "Замена таймера")
        entries = log.get_entries()
        self.assertEqual(len(entries), 3)

    def test_far_dates(self):
        log = RepairLog()
        future = date.today() + timedelta(days=365)
        past = date.today() - timedelta(days=365)
        log.add_entry("Свет", past, 20, "Лампа", "Лампа перегорела")
        log.add_entry("Свет", future, 20, "Лампа", "Лампа перегорела")
        entries = log.get_entries()
        self.assertEqual(len(entries), 2)

    def test_many_items(self):
        log = RepairLog()
        for i in range(10):
            log.add_entry(f"Вещь_{i}", date.today(), 10, "Ремонт", "Ремонт")
        entries = log.get_entries()
        self.assertEqual(len(entries), 10)

    def test_large_cost(self):
        log = RepairLog()
        log.add_entry("Дом", date.today(), 100000, "Ремонт крыши", "Ремонт крыши")
        entries = log.get_entries()
        self.assertEqual(entries[0].cost, 100000)

    def test_special_characters_in_notes(self):
        log = RepairLog()
        log.add_entry("Вещь", date.today(), 0, "Ремонт", "Проблема: 'не работает'")
        entries = log.get_entries()
        self.assertIn("не работает", entries[0].notes)

    def test_special_characters_in_description(self):
        log = RepairLog()
        log.add_entry("Вещь", date.today(), 0, "Замена: 'деталь'", "Замена детали")
        entries = log.get_entries()
        self.assertEqual(entries[0].description, "Замена: 'деталь'")

if __name__ == "__main__":
    unittest.main()
