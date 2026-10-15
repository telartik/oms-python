from product import Product
from customer import Customer

class Cart:
    def __init__(self, cart_id: int, customer: Customer):
        self.cart_id = cart_id
        self.customer = customer
        self.products: list[Product] = []
        self.total_price: float = 0.0

    def add_product(self, product: Product):
        self.products.append(product)
        self.total_price += product.price
        print(f"Товар '{product.name}' додано до кошика")

    def show_cart(self):
        print(f"\nКошик №{self.cart_id}")
        print(f"Клієнт: {self.customer.name} {self.customer.surname}")
        print("Товари:")
        for product in self.products:
            print(f"- {product.name}: {product.price} грн")
        print(f"Загальна сума: {self.total_price} грн")
