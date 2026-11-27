import json
import logging
from pathlib import Path
from typing import Any

from interfaces import Notifier, OrderRepository


class JsonOrderRepository(OrderRepository):
    def __init__(self, file_path: str = "orders.json", logger: logging.Logger | None = None):
        self.file_path = Path(file_path)
        self.logger = logger or logging.getLogger(__name__)

    def save_order(self, order_data: dict[str, Any]) -> None:
        orders = self.load_orders()
        orders.append(order_data)

        with self.file_path.open("w", encoding="utf-8") as f:
            json.dump(orders, f, ensure_ascii=False, indent=2)

        self.logger.info(
            "Замовлення #%s збережено у файл '%s'",
            order_data.get("order_id"),
            self.file_path,
        )

    def load_orders(self) -> list[dict[str, Any]]:
        if not self.file_path.exists():
            self.logger.warning(
                "Файл '%s' ще не існує, повертаємо порожній список",
                self.file_path,
            )
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                self.logger.warning(
                    "Некоректний формат даних у '%s', повертаємо []",
                    self.file_path,
                )
                return []
        except json.JSONDecodeError as exc:
            self.logger.error("Помилка читання JSON із '%s': %s", self.file_path, exc)
            return []


class ConsoleNotifier(Notifier):
    def __init__(self, logger: logging.Logger | None = None):
        self.logger = logger or logging.getLogger(__name__)

    def notify(self, message: str) -> None:
        self.logger.info("Сповіщення: %s", message)
