from order import Order

class Delivery:
    def __init__(self, delivery_id: int, order: Order, address: str, courier: str, price: float):
        self.delivery_id = delivery_id
        self.order = order
        self.address = address
        self.courier = courier
        self.price = price
        self.status = "Підготовка"

    def start_delivery(self):
        self.status = "В дорозі"
        print(f"Замовлення №{self.order.order_id} передано кур'єру")

    def complete_delivery(self):
        self.status = "Доставлено"
        print(f"Замовлення №{self.order.order_id} доставлено \n")

    def show_delivery(self):
        print(
            f"\nДоставка №{self.delivery_id} \n"
            f"Адреса: {self.address} \n"
            f"Кур'єр: {self.courier} \n"
            f"Ціна: {self.price} грн \n"
            f"Статус: {self.status} \n"
        )
