
from playwright.sync_api import Page
from pages.saucedemo import SaucedemoPage


# Test credentials
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


# Reusable login function
def login_to_saucedemo(saucedemo):

    saucedemo.open_website()
    saucedemo.enter_credentials(USERNAME, PASSWORD)
    saucedemo.click_login()
    saucedemo.verify_login_success()


# TC_001: Invalid Login Testing
def test_invalid_login(page: Page):

    saucedemo = SaucedemoPage(page)

    saucedemo.open_website()

    saucedemo.enter_credentials(
        "invalid_user",
        "wrong_password"
    )

    saucedemo.click_login()

    # Verify error message
    saucedemo.verify_login_error()


# TC_002: Logout Testing
def test_logout(page: Page):

    saucedemo = SaucedemoPage(page)

    login_to_saucedemo(saucedemo)

    # Logout
    saucedemo.logout()

    # Verify logout
    saucedemo.verify_logout()


# TC_003: Remove Product from Cart
def test_remove_product_from_cart(page: Page):

    saucedemo = SaucedemoPage(page)

    login_to_saucedemo(saucedemo)

    # Add product
    saucedemo.add_product_to_cart()

    # Verify cart badge
    saucedemo.verify_cart_badge()

    # Open cart
    saucedemo.open_cart()

    # Verify product
    saucedemo.verify_product_in_cart()

    # Remove product
    saucedemo.remove_product_from_cart()

    # Verify cart empty
    saucedemo.verify_cart_empty()


# TC_004: Checkout Testing
def test_checkout(page: Page):

    saucedemo = SaucedemoPage(page)

    login_to_saucedemo(saucedemo)

    # Add product
    saucedemo.add_product_to_cart()

    # Open cart
    saucedemo.open_cart()

    # Verify product
    saucedemo.verify_product_in_cart()

    # Click checkout
    saucedemo.click_checkout()

    # Enter customer details
    saucedemo.enter_checkout_details(
        "Damith",
        "QA",
        "70000"
    )

    # Continue checkout
    saucedemo.click_continue()

    # Finish order
    saucedemo.click_finish()

    # Verify order success
    saucedemo.verify_checkout_success()


# TC_005: Login and Add to Cart
def test_login_and_add_to_cart(page: Page):

    saucedemo = SaucedemoPage(page)

    login_to_saucedemo(saucedemo)

    saucedemo.verify_products_page()

    saucedemo.add_product_to_cart()

    saucedemo.verify_cart_badge()

    saucedemo.open_cart()

    saucedemo.verify_product_in_cart()
