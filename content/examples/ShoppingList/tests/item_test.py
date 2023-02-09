from shopping_list import ShoppingListItem


def test_default_args():
    item = ShoppingListItem("Coffee")
    assert item.amount == "1"
