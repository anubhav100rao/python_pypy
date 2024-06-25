from shopping_cart import ShoppingCart
import pytest
from typing import Dict


@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_can_add_item():
    cart = ShoppingCart()
    pre_size = cart.size()
    cart.add("apple")
    assert pre_size + 1 == cart.size()


def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart()
    cart.add("apple")

    assert "apple" in cart.get_items()


def test_add_capacity():
    cart = ShoppingCart()
    with pytest.raises(OverflowError):
        for _ in range(6):
            cart.add("apple")


def test_get_total_price():
    cart = ShoppingCart()
    cart.add("apple")
    cart.add("orange")

    price_map: Dict[str, int] = {
        "apple": 1,
        "orange": 2
    }

    assert cart.get_total_price(price_map=price_map) == 3
