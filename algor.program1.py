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

class Cart():
    def __init__(self, cart_id, customer, products, total_price, status, creation_date):
        self.cart_id = cart_id
        self.customer = customer
        self.products = products
        self.total_price = total_price
        self.status = status
        self.creation_date = creation_date

    def add_product(self, product):
        self.products.append(product)
        self.total_price += product.price
        print(f"Товар '{product.name}' додано до кошика")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            self.total_price -= product.price
            print(f"Товар '{product.name}' видалено з кошика")
        else:
            print(f"Товару '{product.name}' немає в кошику")

    def show_cart(self):
        print(f"\nКошик №{self.cart_id}")
        print(f"Клієнт: {self.customer.name} {self.customer.surname}")
        print("Товари:")

        for product in self.products:
            print(f"- {product.name}: {product.price} грн")

        print(f"Загальна сума: {self.total_price} грн")


class Order():
    def __init__(self, order_id, customer, products, total_price, status, order_date):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.total_price = total_price
        self.status = status
        self.order_date = order_date

    def calculate_total(self):
        self.total_price = 0

        for product in self.products:
            self.total_price += product.price

        return self.total_price

    def change_status(self, new_status):
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

        
class Payment():
    def __init__(self, payment_id, order, amount, method, status, date):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.method = method
        self.status = status
        self.date = date

    def pay(self):
        if self.order.customer.balance >= self.amount:
            self.order.customer.balance -= self.amount
            self.status = "Оплачено"
            print(f"Замовлення №{self.order.order_id} успішно оплачено")
        else:
            self.status = "Не оплачено"
            print("Недостатньо коштів для оплати")

    def cancel_payment(self):
        self.status = "Скасовано"
        print("Оплату скасовано")

    def show_payment(self):
        print(
            f"\nОплата №{self.payment_id} \n"
            f"Сума: {self.amount} грн \n"
            f"Метод: {self.method} \n"
            f"Статус: {self.status}"
        )