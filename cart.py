from product import Product
from customer import Customer

class Cart:
    def __init__(self, cart_id: int, customer: Customer):
        self.cart_id = cart_id
        self.customer = customer
        self.products: list[Product] = []

    @property
    def total_price(self) -> float:
        return sum(product.price for product in self.products)

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"Товар '{product.name}' додано до кошика")

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
            print(f"Товар '{product.name}' видалено з кошика")
        else:
            print(f"Товару '{product.name}' немає в кошику")

    def __str__(self) -> str:
        if not self.products:
            products_list = "- Кошик порожній"
        else:
            products_list = "\n".join([f"- {p.name}: {p.price} грн" for p in self.products])
            
        return (
            f"\nКошик №{self.cart_id}\n"
            f"Клієнт: {self.customer.name} {self.customer.surname}\n"
            f"Товари:\n{products_list}\n"
            f"Загальна сума: {self.total_price} грн"
        )
