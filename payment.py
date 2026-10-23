from order import Order

class Payment:
    def __init__(self, payment_id: int, order: Order, amount: float, method: str):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.method = method
        self.status = "Очікує оплати"

    def pay(self):
        if self.order.customer.withdraw_money(self.amount):
            self.status = "Оплачено"
            print(f"Замовлення №{self.order.order_id} успішно оплачено")
        else:
            self.status = "Не оплачено"
            print("Недостатньо коштів для оплати")

    def __str__(self) -> str:
        return (
            f"\nОплата №{self.payment_id}\n"
            f"Сума: {self.amount} грн\n"
            f"Метод: {self.method}\n"
            f"Статус: {self.status}"
        )


class CardPayment(Payment):
    """Принцип успадкування ООП: спеціалізований платіж карткою"""
    def __init__(self, payment_id: int, order: Order, amount: float):
        super().__init__(payment_id, order, amount, method="Банківська картка")
