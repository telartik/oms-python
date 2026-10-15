from customer import Customer
from product import Product

class Order:
    def __init__(self, order_id: int, customer: Customer, products: list[Product], order_date: str):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.status = "Створено"
        self.order_date = order_date
        self.total_price = 0.0

    def calculate_total(self) -> float:
        self.total_price = sum(product.price for product in self.products)
        return self.total_price

    def change_status(self, new_status: str):
        self.status = new_status
        print(f"Статус замовлення змінено на: {new_status}")

    def show_order(self):
        print(
            f"\nЗамовлення №{self.order_id} \n"
            f"Клієнт: {self.customer.name} {self.customer.surname} \n"
            f"Сума: {self.total_price} грн \n"
            f"Статус: {self.status} \n"
            f"Дата: {self.order_date} \n"
        )
