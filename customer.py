class Customer:
    def __init__(self, name: str, surname: str, phone: str, address: str, balance: float):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.address = address
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def withdraw_money(self, amount: float) -> bool:
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def show_info(self):
        print(
            f"{self.name} {self.surname}\n"
            f"Телефон: {self.phone}\n"
            f"Баланс: {self._balance} грн\n"
        )
