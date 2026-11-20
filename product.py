class Product:
    def __init__(self, name: str, price: float, category: str, product_id: int, brand: str):
        self.name = name
        self._price = price
        self.category = category
        self.product_id = product_id
        self.brand = brand

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = value

    def requires_delivery(self) -> bool:
        return True

    def purchase(self, quantity: int = 1) -> str:
        return f"Оформлено товар '{self.name}' (кількість: {quantity})"

    def __str__(self) -> str:
        return (
            f"{self.name} (ID: {self.product_id})\n"
            f"Бренд: {self.brand} | Категорія: {self.category}\n"
            f"Ціна: {self._price} грн"
        )


class PhysicalProduct(Product):
    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        product_id: int,
        brand: str,
        stock_quantity: int,
        weight_kg: float,
    ):
        super().__init__(name, price, category, product_id, brand)
        self.stock_quantity = stock_quantity
        self.weight_kg = weight_kg

    def requires_delivery(self) -> bool:
        return True

    def purchase(self, quantity: int = 1) -> str:
        if quantity <= 0:
            return f"Некоректна кількість для '{self.name}'"
        if self.stock_quantity < quantity:
            return f"Недостатньо товару '{self.name}' на складі (доступно: {self.stock_quantity})"
        self.stock_quantity -= quantity
        return (
            f"Фізичний товар '{self.name}' ({quantity} шт., {self.weight_kg * quantity:.2f} кг) "
            f"списано зі складу. Залишок: {self.stock_quantity} шт."
        )

    def __str__(self) -> str:
        base_info = super().__str__()
        return (
            f"{base_info}\n"
            f"Тип: Фізичний товар | Вага: {self.weight_kg} кг | На складі: {self.stock_quantity} шт."
        )


class DigitalProduct(Product):
    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        product_id: int,
        brand: str,
        license_key: str,
        file_size_mb: float,
    ):
        super().__init__(name, price, category, product_id, brand)
        self.license_key = license_key
        self.file_size_mb = file_size_mb

    def requires_delivery(self) -> bool:
        return False

    def purchase(self, quantity: int = 1) -> str:
        return (
            f"Цифровий товар '{self.name}' ({self.file_size_mb} МБ) активовано. "
            f"Ключ доступу: {self.license_key} (доставка кур'єром не потрібна)"
        )

    def __str__(self) -> str:
        base_info = super().__str__()
        return (
            f"{base_info}\n"
            f"Тип: Цифровий товар | Розмір: {self.file_size_mb} МБ | Ключ: {self.license_key}"
        )
