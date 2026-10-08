import pytest
from playwright.sync_api import expect

from interview_task.pages import InventoryPage

pytestmark = pytest.mark.ui


def test_inventory_lists_products(inventory_page: InventoryPage) -> None:
    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.items).to_have_count(6)


def test_add_item_to_cart(inventory_page: InventoryPage) -> None:
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


def test_sort_by_price_low_to_high(inventory_page: InventoryPage) -> None:
    inventory_page.sort_by("Price (low to high)")
    prices = inventory_page.prices()
    assert prices == sorted(prices)
