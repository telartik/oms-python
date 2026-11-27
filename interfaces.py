from abc import ABC, abstractmethod
from typing import Any


class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order_data: dict[str, Any]) -> None:
        pass

    @abstractmethod
    def load_orders(self) -> list[dict[str, Any]]:
        pass


class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass
