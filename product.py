class Product:
    def __init__(self, name: str, price: float, category: str, quantity: int, product_id: int, brand: str):
        self.name = name
        self._price = price
        self.category = category
        self.quantity = quantity
        self.product_id = product_id
        self.brand = brand

    @property
    def price(self) -> float:
        return self._price

    def show_info(self):
        print(
            f"{self.name}\n"
            f"{self.brand}\n"
            f"{self.category}\n"
            f"{self.price} грн\n"
            f"На складі: {self.quantity}\n"
        )
