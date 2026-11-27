import logging
import tempfile
import unittest
from pathlib import Path

from cart import Cart
from checkout_service import CheckoutService
from customer import Customer
from delivery import DeliveryGraph
from interfaces import Notifier
from order import Order
from payment import Payment
from product import DigitalProduct, PhysicalProduct
from storage import JsonOrderRepository


class DummyNotifier(Notifier):
    def __init__(self) -> None:
        self.messages: list[str] = []

    def notify(self, message: str) -> None:
        self.messages.append(message)


class TestShopSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = logging.getLogger("test_logger")
        self.logger.disabled = True

        self.customer = Customer("Олена", "Коваль", "+380501234567", "Центр", 5000.0)
        self.book = PhysicalProduct(
            "Книга Python",
            600.0,
            "Книги",
            1,
            "BookHouse",
            stock_quantity=3,
            weight_kg=0.5,
        )
        self.ebook = DigitalProduct(
            "Електронна книга",
            300.0,
            "Книги",
            2,
            "BookHouse",
            "KEY",
            15.3,
        )

        self.graph = DeliveryGraph()
        self.graph.add_edge("Склад", "Центр", 4.0)

    def test_cart_total_and_remove(self) -> None:
        cart = Cart(1, self.customer)
        cart.add_product(self.book)
        cart.add_product(self.ebook)
        self.assertEqual(cart.total_price, 900.0)

        cart.remove_product(self.ebook)
        self.assertEqual(cart.total_price, 600.0)

    def test_price_setter_rejects_negative(self) -> None:
        with self.assertRaises(ValueError):
            self.book.price = -10.0

    def test_polymorphism_products(self) -> None:
        self.assertTrue(self.book.requires_delivery())
        self.assertFalse(self.ebook.requires_delivery())

        msg = self.book.purchase(2)
        self.assertIn("Залишок: 1 шт.", msg)
        self.assertEqual(self.book.stock_quantity, 1)

    def test_delivery_graph_distance(self) -> None:
        self.assertEqual(self.graph.get_distance("Склад", "Центр"), 4.0)
        self.assertEqual(self.graph.get_distance("Склад", "Невідомий"), 0.0)

    def test_json_repository_save_and_load(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = str(Path(tmp_dir) / "orders_test.json")
            repo = JsonOrderRepository(file_path=file_path, logger=self.logger)

            order = Order(10, self.customer, [self.book], "27.11.2026")
            order.calculate_total()
            repo.save_order(order.to_dict())

            loaded = repo.load_orders()
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0]["order_id"], 10)
            self.assertEqual(loaded[0]["total_price"], 600.0)

    def test_checkout_service_with_dependency_injection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = str(Path(tmp_dir) / "checkout_orders.json")
            repo = JsonOrderRepository(file_path=file_path, logger=self.logger)
            notifier = DummyNotifier()
            service = CheckoutService(
                repository=repo,
                notifier=notifier,
                logger=self.logger,
            )

            order = Order(20, self.customer, [self.book], "27.11.2026")
            order.calculate_total()
            payment = Payment(1, order, order.total_price, method="Картка")

            ok = service.process_order(
                order=order,
                payment=payment,
                city_map=self.graph,
                start_point="Склад",
                destination="Центр",
            )

            self.assertTrue(ok)
            self.assertEqual(order.status, "Доставлено")
            self.assertEqual(self.customer.balance, 4400.0)
            self.assertEqual(len(repo.load_orders()), 1)
            self.assertEqual(len(notifier.messages), 1)


if __name__ == "__main__":
    unittest.main()