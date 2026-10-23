from order import Order

class DeliveryGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, node1: str, node2: str, distance: float):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = {}
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = {}
        self.adjacency_list[node1][node2] = distance
        self.adjacency_list[node2][node1] = distance

    def get_distance(self, start: str, end: str) -> float:
        if start in self.adjacency_list and end in self.adjacency_list[start]:
            return self.adjacency_list[start][end]
        return 0.0


class Delivery:
    def __init__(self, delivery_id: int, order: Order, destination: str, courier: str, city_map: DeliveryGraph, start_point: str = "Склад"):
        self.delivery_id = delivery_id
        self.order = order
        self.destination = destination
        self.courier = courier
        self.city_map = city_map
        self.start_point = start_point
        self.status = "Підготовка"
        self.price = self._calculate_price()

    def _calculate_price(self) -> float:
        distance = self.city_map.get_distance(self.start_point, self.destination)
        rate_per_km = 15.0  # 15 грн за 1 км
        return distance * rate_per_km if distance > 0 else 50.0

    def start_delivery(self):
        self.status = "В дорозі"
        print(f"Замовлення №{self.order.order_id} передано кур'єру ({self.courier}). Маршрут: {self.start_point} ➔ {self.destination}")

    def complete_delivery(self):
        self.status = "Доставлено"
        print(f"Замовлення №{self.order.order_id} успішно доставлено\n")

    def __str__(self) -> str:
        distance = self.city_map.get_distance(self.start_point, self.destination)
        return (
            f"\nДоставка №{self.delivery_id}\n"
            f"Маршрут: {self.start_point} ➔ {self.destination} ({distance} км)\n"
            f"Кур'єр: {self.courier}\n"
            f"Ціна доставки: {self.price} грн\n"
            f"Статус: {self.status}"
        )
