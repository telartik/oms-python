class Product():
    def __init__(self, name, price, category, quantity, product_id, brand):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        self.product_id = product_id
        self.brand = brand

    def reduce_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"Кількість товару '{self.name}' зменшено на {amount}")
        else:
            print(f"Недостатньо товару '{self.name}' на складі")

    def add_quantity(self, amount):
        self.quantity += amount
        print(f"Кількість товару '{self.name}' збільшено на {amount}")

    def show_info(self):
        print(
            f"{self.name}\n"
            f"{self.brand}\n"
            f"{self.category}\n"
            f"{self.price} грн\n"
            f"На складі: {self.quantity}\n"
        )


class Customer():
    def __init__(self, name, surname, email, phone, address, balance):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.address = address
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        print(f"Баланс клієнта поповнено на {amount} грн")

    def change_address(self, new_address):
        self.address = new_address
        print(f"Адресу клієнта змінено на: {new_address}")

    def show_info(self):
        print(
            f"{self.name} {self.surname}\n"
            f"Телефон: {self.phone}\n"
            f"Баланс: {self.balance} грн\n"
        )
