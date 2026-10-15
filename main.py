from product import Product
from customer import Customer
from cart import Cart
from order import Order
from payment import CardPayment
from delivery import Delivery


def main():
    product1 = Product("Ноутбук Lenovo", 25000, "Електроніка", 5, 101, "Lenovo")
    product2 = Product("Мишка Logitech", 800, "Комп'ютерні аксесуари", 20, 102, "Logitech")

    customer1 = Customer(
        "Іван",
        "Ткач",
        "+380971112233",
        "м. Вінниця, вул. Політехнічна, 5",
        30000
    )

    cart1 = Cart(1, customer1)
    cart1.add_product(product1)
    cart1.add_product(product2)
    cart1.show_cart()

    order1 = Order(1, customer1, cart1.products, "08.10.2026")
    order1.calculate_total()
    order1.show_order()

    payment1 = CardPayment(1, order1, order1.total_price)
    payment1.pay()
    payment1.show_payment()

    delivery1 = Delivery(1, order1, customer1.address, "Нова Пошта", 100)
    delivery1.show_delivery()

    delivery1.start_delivery()
    delivery1.show_delivery()

    order1.change_status("Відправлено")
    delivery1.complete_delivery()

    print("- Товари -")
    product1.show_info()
    product2.show_info()

    print("- Клієнт -")
    customer1.show_info()


if __name__ == "__main__":
    main()
