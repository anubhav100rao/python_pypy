from typing import List, Dict


class ShoppingCart:
    def __init__(self, MAX_SIZE=5) -> None:
        self.items: List[str] = []
        self.MAX_SIZE = MAX_SIZE

    def add(self, item: str) -> None:
        if self.size() == self.MAX_SIZE:
            raise OverflowError(
                "Cart is at its max capacity, can't add more elements"
            )
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map: Dict[str, int]) -> int:
        total: int = 0
        for item in self.items:
            total += price_map.get(item, 0)
        return total
