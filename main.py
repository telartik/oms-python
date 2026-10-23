from product import Product
from customer import Customer
from cart import Cart
from order import Order
from payment import CardPayment
from delivery import Delivery, DeliveryGraph


def main():
    # 1. Створюємо розгалужену карту міста (граф логістики)
    city_map = DeliveryGraph()
    
    # Додаємо дороги від головного складу до різних районів міста (з різною відстанню в км)
    city_map.add_edge("Склад", "Центр", 5.0)
    city_map.add_edge("Склад", "Вишенька", 9.2)
    city_map.add_edge("Склад", "Поділля", 6.5)
    city_map.add_edge("Склад", "Замостя", 4.0)

    # 2. Створюємо товари та клієнта
    product1 = Product("Ноутбук Lenovo", 25000, "Електроніка", 5, 101, "Lenovo")
    product2 = Product("Мишка Logitech", 800, "Комп'ютерні аксесуари", 20, 102, "Logitech")

    # Клієнт живе, наприклад, у районі "Вишенька"
    customer_district = "Вишенька"
    customer1 = Customer(
        "Іван",
        "Ткач",
        "+380971112233",
        f"м. Вінниця, район {customer_district}",
        30000
    )

    # 3. Робота з кошиком
    cart1 = Cart(1, customer1)
    cart1.add_product(product1)
    cart1.add_product(product2)
    print(cart1)

    # Видаляємо один товар (перевіряємо динамічний розрахунок суми)
    cart1.remove_product(product2)
    print(cart1)

    # 4. Створення замовлення
    order1 = Order(1, customer1, cart1.products, "08.10.2026")
    order1.calculate_total()
    print(order1)

    # 5. Оплата замовлення
    payment1 = CardPayment(1, order1, order1.total_price)
    payment1.pay()
    print(payment1)

    # 6. Доставка з автоматичним розрахунком через граф
    delivery1 = Delivery(
        delivery_id=1,
        order=order1,
        destination=customer_district,   пункт призначення тепер збігається з вершиною графа
        courier="Нова Пошта",
        city_map=city_map,
        start_point="Склад"
    )
    print(delivery1)  # Тут ціна порахується автоматично: 9.2 км * 15 грн = 138 грн!

    delivery1.start_delivery()
    order1.change_status("Відправлено")
    delivery1.complete_delivery()

    # 7. Вивід інформації через магічний метод __str__
    print("- Товари -")
    print(product1)
    print(product2)

    print("\n- Клієнт -")
    print(customer1)


if __name__ == "__main__":
    main()
