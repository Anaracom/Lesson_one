# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: RepairLog
class TagManager:
    _tags = {}
    
    @classmethod
    def add_tag(cls, name):
        if not cls._tags.get(name):
            cls._tags[name] = []
            return True
        return False
    
    @classmethod
    def remove_tag(cls, name):
        removed_count = len(cls._tags.pop(name, []))
        del cls._tags[name]
        return removed_count
