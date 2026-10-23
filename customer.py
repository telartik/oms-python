class Customer:
    def __init__(self, name: str, surname: str, phone: str, address: str, balance: float):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.address = address
        self._balance = balance  # Інкапсуляція балансу

    @property
    def balance(self) -> float:
        return self._balance

    def withdraw_money(self, amount: float) -> bool:
        """Безпечне зняття кошти з перевіркою"""
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def __str__(self) -> str:
        return (
            f"Клієнт: {self.name} {self.surname}\n"
            f"Телефон: {self.phone}\n"
            f"Адреса: {self.address}\n"
            f"Баланс: {self._balance} грн"
        )
