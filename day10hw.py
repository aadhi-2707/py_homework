from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):  # fixed __init__
        self.name = name
        self.account_year = account_year

    def account_age(self):
        current_year = 2025
        return current_year - self.account_year

    @abstractmethod
    def get_role(self):
        pass


class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):  # fixed __str__
        return f"[Admin] Name: {self.name}, Account Age: {self.account_age()} years"


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):  # fixed __str__
        return f"[Guest] Name: {self.name}, Account Age: {self.account_age()} years"


# -------- Example Usage --------
admin_user = Admin("Alice", 2020)
guest_user = Guest("Bob", 2023)

for user in (admin_user, guest_user):
    print("Role:", user.get_role())
    print("Account Age:", user.account_age(), "years")
    print(user)  # __str__ will be called
    print()
