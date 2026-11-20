from product import PhysicalProduct, DigitalProduct
from customer import Customer
from cart import Cart
from order import Order
from payment import Payment
from delivery import Delivery, DeliveryGraph


def main():
    city_map = DeliveryGraph()
    city_map.add_edge("Склад", "Центр", 5.0)
    city_map.add_edge("Склад", "Вишенька", 9.2)
    city_map.add_edge("Склад", "Поділля", 6.5)
    city_map.add_edge("Склад", "Замостя", 4.0)

    laptop = PhysicalProduct(
        name="Ноутбук Lenovo",
        price=25000,
        category="Електроніка",
        product_id=101,
        brand="Lenovo",
        stock_quantity=5,
        weight_kg=1.8,
    )
    mouse = PhysicalProduct(
        name="Мишка Logitech",
        price=800,
        category="Аксесуари",
        product_id=102,
        brand="Logitech",
        stock_quantity=20,
        weight_kg=0.15,
    )
    antivirus = DigitalProduct(
        name="Антивірус Pro (1 рік)",
        price=1200,
        category="Програмне забезпечення",
        product_id=201,
        brand="Avast",
        license_key="CG-2026-X9K4-8821",
        file_size_mb=420.0,
    )

    customer_district = "Вишенька"
    customer1 = Customer(
        "Іван",
        "Ткач",
        "+380971112233",
        f"м. Вінниця, район {customer_district}",
        30000,
    )

    cart1 = Cart(1, customer1)
    cart1.add_product(laptop)
    cart1.add_product(mouse)
    cart1.add_product(antivirus)
    cart1.remove_product(mouse)
    print(cart1)

    order1 = Order(1, customer1, cart1.products, "19.11.2026")
    order1.calculate_total()
    print(order1)

    payment1 = Payment(1, order1, order1.total_price, method="Картка / Баланс")
    if payment1.pay():
        print("\n- Обробка товарів замовлення -")
        for item in order1.products:
            print(item.purchase(1))
    print(payment1)

    has_physical_items = any(item.requires_delivery() for item in order1.products)
    if has_physical_items:
        delivery1 = Delivery(
            delivery_id=1,
            order=order1,
            destination=customer_district,
            courier="Нова Пошта",
            city_map=city_map,
            start_point="Склад",
        )
        print(delivery1)
        delivery1.start_delivery()
        order1.change_status("Відправлено")
        delivery1.complete_delivery()
    else:
        order1.change_status("Доставлено (цифровий контент)")

    print("\n- Усі товари -")
    for item in (laptop, mouse, antivirus):
        print(item)
        print("-" * 30)

    print("\n- Клієнт -")
    print(customer1)


if __name__ == "__main__":
    main()
