from product import Product
from customer import Customer
from cart import Cart
from order import Order
from payment import CardPayment
from delivery import Delivery, DeliveryGraph


def main():
    city_map = DeliveryGraph()
    city_map.add_edge("Склад", "Центр", 5.0)
    city_map.add_edge("Центр", "м. Вінниця, вул. Політехнічна, 5", 3.5)

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
    print(cart1)

    cart1.remove_product(product2)
    print(cart1)

    order1 = Order(1, customer1, cart1.products, "08.10.2026")
    order1.calculate_total()
    print(order1)

    payment1 = CardPayment(1, order1, order1.total_price)
    payment1.pay()
    print(payment1)

    delivery1 = Delivery(
        delivery_id=1,
        order=order1,
        destination=customer1.address,
        courier="Нова Пошта",
        city_map=city_map,
        start_point="Склад"
    )
    print(delivery1)

    delivery1.start_delivery()
    order1.change_status("Відправлено")
    delivery1.complete_delivery()

    print("- Товари -")
    print(product1)
    print(product2)

    print("\n- Клієнт -")
    print(customer1)


if __name__ == "__main__":
    main()
