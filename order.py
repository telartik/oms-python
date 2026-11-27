from typing import Any
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

    def change_status(self, new_status: str) -> None:
        self.status = new_status

    def to_dict(self) -> dict[str, Any]:
        return {
            "order_id": self.order_id,
            "customer": f"{self.customer.name} {self.customer.surname}",
            "address": self.customer.address,
            "order_date": self.order_date,
            "status": self.status,
            "total_price": self.total_price,
            "items": [
                {
                    "product_id": p.product_id,
                    "name": p.name,
                    "price": p.price,
                    "requires_delivery": p.requires_delivery(),
                }
                for p in self.products
            ],
        }

    def __str__(self) -> str:
        return (
            f"\nЗамовлення №{self.order_id}\n"
            f"Клієнт: {self.customer.name} {self.customer.surname}\n"
            f"Сума: {self.total_price} грн\n"
            f"Статус: {self.status}\n"
            f"Дата: {self.order_date}"
        )
