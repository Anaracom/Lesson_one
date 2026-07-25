# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: RepairLog
class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self.active_profile = None
    
    def add_profile(self, name, initial_balance=0.0):
        self.profiles[name] = RepairLog(initial_balance)
        if not self.active_profile:
            self.set_active(name)
    
    def set_active(self, profile_name):
        if profile_name in self.profiles:
            self.active_profile = self.profiles[profile_name]
            return True
        else:
            print(f"Профиль '{profile_name}' не найден")
            return False
    
    def get_active(self):
        return self.active_profile
