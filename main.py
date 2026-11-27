from cart import Cart
from checkout_service import CheckoutService
from customer import Customer
from delivery import DeliveryGraph
from logger_config import setup_logger
from order import Order
from payment import Payment
from product import DigitalProduct, PhysicalProduct
from storage import ConsoleNotifier, JsonOrderRepository


def main() -> None:
    logger = setup_logger(name="online_store", log_file="shop.log")

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
        brand="CyberGuard",
        license_key="CG-2026-X9K4-8821",
        file_size_mb=420.0,
    )

    customer_district = "Вишенька"
    customer1 = Customer(
        name="Іван",
        surname="Ткач",
        phone="+380971112233",
        address=f"м. Вінниця, район {customer_district}",
        balance=30000,
    )

    cart1 = Cart(1, customer1)
    cart1.add_product(laptop)
    cart1.add_product(mouse)
    cart1.add_product(antivirus)
    cart1.remove_product(mouse)

    order1 = Order(1, customer1, cart1.products, "27.11.2026")
    payment1 = Payment(1, order1, cart1.total_price, method="Картка / Баланс")

    repository = JsonOrderRepository(file_path="orders.json", logger=logger)
    notifier = ConsoleNotifier(logger=logger)
    checkout = CheckoutService(repository=repository, notifier=notifier, logger=logger)

    checkout.process_order(
        order=order1,
        payment=payment1,
        city_map=city_map,
        start_point="Склад",
        destination=customer_district,
        courier="Нова Пошта",
    )

    saved_orders = repository.load_orders()
    logger.info("Усього збережених замовлень у файлі: %d", len(saved_orders))


if __name__ == "__main__":
    main()
