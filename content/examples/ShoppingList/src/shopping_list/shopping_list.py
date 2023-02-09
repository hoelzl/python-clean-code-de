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
        """Create a shopping list from item values.

        Each item value in `item_values` is a tuple of product name and amount.
        >>> ShoppingList.from_item_values([("Tea", "500g"), ("Coffee", "2 packs")])
        ShoppingList(items=[ShoppingListItem(product='Tea', amount='500g'),
                            ShoppingListItem(product='Coffee', amount='2 packs')])
        """
        items = [ShoppingListItem(product, amount) for product, amount in item_values]
        return ShoppingList(items)

    def __str__(self):
        """Convert a shopping list into a string.

        >>> print(ShoppingList().from_item_values(
        ...         [("Tea", "500g"), ("Coffee", "2 packs")]))
        Shopping List
          Tea (500g)
          Coffee (2 packs)
        <BLANKLINE>
        """
        result = "Shopping List\n"
        for item in self.items:
            result += f"  {item.product} ({item.amount})\n"
        return result

    def __len__(self):
        """Return the number of items in a shopping list.

        >>> len(ShoppingList())
        0
        >>> len(ShoppingList.from_item_values([("Tea", "500g"), ("Coffee", "2 packs")]))
        2
        """
        return len(self.items)

    def __getitem__(self, n):
        """Return an item, either by index or product name.

        >>> sl = ShoppingList.from_item_values([("Tea", "500g"), ("Coffee", "2 packs")])
        >>> sl[0]
        ShoppingListItem(product='Tea', amount='500g')
        >>> sl["Tea"]
        ShoppingListItem(product='Tea', amount='500g')
        >>> sl["Coffee"]
        ShoppingListItem(product='Coffee', amount='2 packs')
        >>> sl["Water"] is None
        True
        """
        if isinstance(n, str):
            return self.find_product(n)
        return self.items[n]

    def find_product(self, product: str):
        """Find an item given its product.

        >>> sl = ShoppingList.from_item_values([("Tea", "500g"), ("Coffee", "2 packs")])
        >>> sl.find_product("Tea")
        ShoppingListItem(product='Tea', amount='500g')
        >>> sl.find_product("Coffee")
        ShoppingListItem(product='Coffee', amount='2 packs')
        """
        for item in self.items:
            if item.product == product:
                return item
        return None

    def add_item(self, item: ShoppingListItem):
        """Add an item to a shopping list if it is not already in the list.

        Raises an error of type `ValueError` if an item with the same product name
        is already contained in the shopping list.

        >>> sl = ShoppingList()
        >>> sl.add_item(ShoppingListItem("Coffee"))
        >>> sl
        ShoppingList(items=[ShoppingListItem(product='Coffee', amount='1')])
        >>> sl.add_item(ShoppingListItem("Coffee", "500g"))
        Traceback (most recent call last):
        ...
        ValueError: Shopping list already contains Coffee.
        """
        if self.find_product(item.product):
            raise ValueError(f"Shopping list already contains {item.product}.")
        self.items.append(item)
