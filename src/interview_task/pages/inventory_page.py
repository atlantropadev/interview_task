from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.sort_select = page.locator("[data-test='product-sort-container']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")

    def add_to_cart(self, item_name: str) -> None:
        self.items.filter(has_text=item_name).get_by_role("button", name="Add to cart").click()

    def sort_by(self, label: str) -> None:
        self.sort_select.select_option(label=label)

    def prices(self) -> list[float]:
        return [float(p.removeprefix("$")) for p in self.item_prices.all_inner_texts()]
