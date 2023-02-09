from dataclasses import dataclass, field  # noqa
from typing import Sequence


@dataclass
class ShoppingListItem:
    product: str
    amount: str = field(default="1")


@dataclass
class ShoppingList:
    items: list[ShoppingListItem] = field(default_factory=list)

    @staticmethod
    def from_item_values(item_values: Sequence[tuple[str, str]]):
        items = [ShoppingListItem(product, amount) for product, amount in item_values]
        return ShoppingList(items)

    def __str__(self):
        result = "Shopping List\n"
        for item in self.items:
            result += f"  {item.product} ({item.amount})\n"
        return result

    def __len__(self):
        return len(self.items)

    def __getitem__(self, n):
        if isinstance(n, str):
            return self.find_product(n)
        return self.items[n]

    def find_product(self, product: str):
        for item in self.items:
            if item.product == product:
                return item
        return None

    def add_item(self, item: ShoppingListItem):
        if self.find_product(item.product):
            raise ValueError(f"Shopping list already contains {item.product}.")
        self.items.append(item)
