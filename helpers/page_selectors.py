from typing import Tuple
from selenium.webdriver.common.by import By

def get_button_selector(item_name: str, button_type: str) -> Tuple[By, str]:
    """
    Constructs a CSS selector for a button based on the item name and button type.

    Args:
        item_name (str): The name of the item for which the button is being selected.
        button_type (str): The type of the button (e.g., 'add_to_cart', 'remove').

    Returns:
        Tuple[By, str]: A tuple containing the selector strategy and the CSS selector string.

    Example:
        selector = get_button_selector("backpack", "add_to_cart")
        # This would return (By.CSS_SELECTOR, "button[data-test='add_to_cart-backpack']")
    """
    return (By.CSS_SELECTOR, f"button[data-test='{button_type}-{item_name}']")


# LOGIN PAGE

USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "input[type='submit']")
LOGIN_ERROR_CONTAINER = (By.CSS_SELECTOR, ".error-message-container")

# HEADER

BURGER_MENU_BTN = (By.CSS_SELECTOR, "button#react-burger-menu-btn")
CART_BTN = (By.CSS_SELECTOR, "a.shopping_cart_link")
FILTERS_DRPDWN_MENU = (By.CSS_SELECTOR, "select.product_sort_container")
HEADER_LOGO = (By.CSS_SELECTOR, ".app_logo")
CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

BURGER_MENU_SUBBTNS = {
    "All Items": (By.CSS_SELECTOR, "a[data-test='inventory-sidebar-link']"),
    "About": (By.CSS_SELECTOR, "a[data-test='about-sidebar-link']"),
    "Logout": (By.CSS_SELECTOR, "a[data-test='logout-sidebar-link']"),
    "Reset App State": (By.CSS_SELECTOR, "a[data-test='reset-sidebar-link']"),
}

SORTING_OPTIONS = {
    "A to Z": {
        "xpath": (By.XPATH, "//option[normalize-space(text())='Name (A to Z)']"),
        "expected_order": 'straight',
        "sorting_value": 'title'
    },
    "Z to A": {
        "xpath": (By.XPATH, "//option[normalize-space(text())='Name (Z to A)']"),
        "expected_order": 'reverse',
        "sorting_value": 'title'
    },
    "Low to High": {
        "xpath": (By.XPATH, "//option[@value='lohi']"),
        "expected_order": 'straight',
        "sorting_value": 'price'
    },
    "High to Low": {
        "xpath": (By.XPATH, "//option[@value='hilo']"),
        "expected_order": 'reverse',
        "sorting_value": 'price'
    }
}


# ITEMS LIST

ITEMS = {
    "Backpack": {
        "image": (By.CSS_SELECTOR, "img[alt='Sauce Labs Backpack']"),
        "add_to_cart": get_button_selector("sauce-labs-backpack", "add-to-cart"),
        "remove": get_button_selector("sauce-labs-backpack", "remove"),
        "title": (By.CSS_SELECTOR, "a#item_4_title_link>div"),
    },
    "Bike Light": {
        "image": (By.CSS_SELECTOR, "img[alt='Sauce Labs Bike Light']"),
        "add_to_cart": get_button_selector("sauce-labs-bike-light", "add-to-cart"),
        "remove": get_button_selector("sauce-labs-bike-light", "remove"),
        "title": (By.CSS_SELECTOR, "a#item_0_title_link>div"),
    },
    "T-Shirt": {
        "image": (By.CSS_SELECTOR, "img[alt='Sauce Labs Bolt T-Shirt']"),
        "add_to_cart": get_button_selector("sauce-labs-bolt-t-shirt", "add-to-cart"),
        "remove": get_button_selector("sauce-labs-bolt-t-shirt", "remove"),
        "title": (By.CSS_SELECTOR, "a#item_1_title_link>div"),
    },
    "Fleece Jacket": {
        "image": (By.CSS_SELECTOR, "img[alt='Sauce Labs Fleece Jacket']"),
        "add_to_cart": get_button_selector("sauce-labs-fleece-jacket", "add-to-cart"),
        "remove": get_button_selector("sauce-labs-fleece-jacket", "remove"),
        "title": (By.CSS_SELECTOR, "a#item_5_title_link>div"),
    },
    "Onesie": {
        "image": (By.CSS_SELECTOR, "img[alt='Sauce Labs Onesie']"),
        "add_to_cart": get_button_selector("sauce-labs-onesie", "add-to-cart"),
        "remove": get_button_selector("sauce-labs-onesie", "remove"),
        "title": (By.CSS_SELECTOR, "a#item_2_title_link>div"),
    },
    "Red T-Shirt": {
        "image": (By.CSS_SELECTOR, "img[alt='Test.allTheThings() T-Shirt (Red)']"),
        "add_to_cart": get_button_selector("test.allthethings()-t-shirt-(red)", "add-to-cart"),
        "remove": get_button_selector("test.allthethings()-t-shirt-(red)", "remove"),
        "title": (By.CSS_SELECTOR, "a#item_3_title_link>div"),
    },
}

# ITEMS CONTAINER

GENERAL_CONTAINER = (By.CSS_SELECTOR, ".inventory_list")
ALL_PRODUCT_CARDS = (By.CSS_SELECTOR, ".inventory_list > *")

# FOOTER

XITTER_BTN = (By.CSS_SELECTOR, "a[data-test='social-twitter']")
FB_BTN = (By.CSS_SELECTOR, "a[data-test='social-facebook']")
LINKEDIN_BTN = (By.CSS_SELECTOR, "a[data-test='social-linkedin']")

# CART

REMOVE_LIGHTS = (By.CSS_SELECTOR, "#remove-sauce-labs-bike-light")
REMOVE_BACKPACK = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
REMOVE_T_SHIRT = (By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")
REMOVE_JACKET = (By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")
REMOVE_T_SHIRT_RED = (By.CSS_SELECTOR, "#remove-test.allthethings()-t-shirt-(red)")
REMOVE_ONESIE = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")

CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, "#continue-shopping")
CHECKOUT_BTN = (By.CSS_SELECTOR, "#checkout")

# CHECKOUT 

FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
ZIP_INPUT = (By.CSS_SELECTOR, "#postal-code")

CANCEL_BTN = (By.CSS_SELECTOR, "#cancel")
CONTINUE_CHECKOUT_BTN = (By.CSS_SELECTOR, "#continue")
FINISH_BTN = (By.CSS_SELECTOR, "#finish")

CHECKOUT_ERROR_CONTATINER = (By.CSS_SELECTOR, "h3[data-test='error']")

BACK_HOME_BTN = (By.CSS_SELECTOR, "#back-to-products")
