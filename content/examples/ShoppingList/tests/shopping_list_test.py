from shopping_list import ShoppingList, ShoppingListItem
import pytest


@pytest.fixture
def shopping_list():
    return ShoppingList.from_item_values([("Tea", "500g"), ("Coffee", "2 packs")])


def test_from_item_values():
    sl = ShoppingList.from_item_values([("Tea", "500g"), ("Coffee", "2 packs")])
    assert type(sl) == ShoppingList
    assert sl.items == [
        ShoppingListItem("Tea", "500g"),
        ShoppingListItem("Coffee", "2 packs"),
    ]


def test_str(shopping_list):
    assert str(shopping_list) == "Shopping List\n  Tea (500g)\n  Coffee (2 packs)\n"


def test_len(shopping_list):
    assert len(shopping_list) == 2


def test_getitem_with_int_index(shopping_list):
    assert shopping_list[0] == ShoppingListItem("Tea", "500g")


def test_getitem_with_string_index(shopping_list):
    assert shopping_list["Tea"] == ShoppingListItem("Tea", "500g")
    assert shopping_list["Water"] is None


def test_find_product(shopping_list):
    assert shopping_list.find_product("Tea") == ShoppingListItem("Tea", "500g")
    assert shopping_list.find_product("Water") is None


def test_add_item():
    sl = ShoppingList()
    sl.add_item(ShoppingListItem("Butter", "500g"))
    assert sl == ShoppingList([ShoppingListItem("Butter", "500g")])
