# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: RepairLog
class UserProfile:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_dict(cls, data):
        return cls(name=data.get("name", ""), email=data.get("email", ""))

    def to_dict(self):
        return {"name": self.name, "email": self.email}


class ProfileManager:
    def __init__(self):
        self.profiles = [UserProfile.from_dict(data) for data in json.loads(open("profiles.json").read())]
        if not self.profiles:
            print("Создание дефолтного профиля...")
            self.add_profile(UserProfile(name="Пользователь", email="user@example.com"))

    def add_profile(self, user):
        self.profiles.append(user)
        with open("profiles.json", "w") as f:
            json.dump([p.to_dict() for p in self.profiles], f, indent=2)

    def get_current(self):
        return self.profiles[-1] if self.profiles else None

    def switch_profile(self, idx):
        if 0 <= idx < len(self.profiles):
            self.profiles[-1] = self.profiles[idx]
            print(f"Переключено на профиль: {self.profiles[idx].name}")
