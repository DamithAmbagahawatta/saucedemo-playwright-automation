
from playwright.sync_api import Page, expect


class SaucedemoPage:

    def __init__(self, page: Page):
        self.page = page

        # Login elements
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

        # Products elements
        self.products_title = page.locator(".title")
        self.add_to_cart_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )
        self.remove_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )

        # Cart elements
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_item = page.locator(".cart_item")

        # Checkout elements
        self.checkout_button = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")

        # Menu elements
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_button = page.locator("#logout_sidebar_link")

    # Open website
    def open_website(self):
        self.page.goto("https://www.saucedemo.com/")

    # Login
    def enter_credentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def verify_login_success(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

    # Invalid login verification
    def verify_login_error(self):
        expect(self.error_message).to_be_visible()

    # Products page verification
    def verify_products_page(self):
        expect(self.products_title).to_have_text("Products")

    # Add product
    def add_product_to_cart(self):
        self.add_to_cart_button.click()

    def verify_cart_badge(self):
        expect(self.cart_badge).to_have_text("1")

    # Open cart
    def open_cart(self):
        self.cart_icon.click()

    def verify_product_in_cart(self):
        expect(self.cart_item).to_have_count(1)
        expect(self.cart_item).to_contain_text(
            "Sauce Labs Backpack"
        )

    # Remove product
    def remove_product_from_cart(self):
        self.remove_button.click()

    def verify_cart_empty(self):
        expect(self.cart_badge).to_have_count(0)
        expect(self.cart_item).to_have_count(0)

    # Logout
    def logout(self):
        self.menu_button.click()
        self.logout_button.click()

    def verify_logout(self):
        expect(self.login_button).to_be_visible()

    # Checkout
    def click_checkout(self):
        self.checkout_button.click()

    def enter_checkout_details(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def click_continue(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()

    def verify_checkout_success(self):
        expect(self.complete_header).to_have_text(
            "Thank you for your order!"
        )
