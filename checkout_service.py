import logging

from delivery import Delivery, DeliveryGraph
from interfaces import Notifier, OrderRepository
from order import Order
from payment import Payment


class CheckoutService:
    def __init__(
        self,
        repository: OrderRepository,
        notifier: Notifier,
        logger: logging.Logger | None = None,
    ):
        self.repository = repository
        self.notifier = notifier
        self.logger = logger or logging.getLogger(__name__)

    def process_order(
        self,
        order: Order,
        payment: Payment,
        city_map: DeliveryGraph,
        start_point: str = "Склад",
        destination: str = "Центр",
        courier: str = "Нова Пошта",
    ) -> bool:
        order.calculate_total()
        self.logger.info(
            "Початок оформлення замовлення #%s на суму %.2f грн",
            order.order_id,
            order.total_price,
        )

        if not payment.pay():
            order.change_status("Помилка оплати")
            self.logger.warning("Оплата замовлення #%s не пройшла", order.order_id)
            self.notifier.notify(f"Замовлення №{order.order_id} не оплачено.")
            return False

        order.change_status("Оплачено")
        for item in order.products:
            result_msg = item.purchase(1)
            self.logger.info(result_msg)

        has_physical = any(item.requires_delivery() for item in order.products)
        if has_physical:
            delivery = Delivery(
                delivery_id=order.order_id,
                order=order,
                destination=destination,
                courier=courier,
                city_map=city_map,
                start_point=start_point,
            )
            delivery.start_delivery()
            order.change_status("В дорозі")
            delivery.complete_delivery()
            order.change_status("Доставлено")
        else:
            order.change_status("Доставлено (цифровий контент)")

        self.repository.save_order(order.to_dict())
        self.notifier.notify(
            f"Замовлення №{order.order_id} успішно оброблено ({order.status})."
        )
        return True