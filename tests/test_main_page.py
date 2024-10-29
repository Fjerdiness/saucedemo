
import pytest
from helpers import base_actions
from helpers.base_settings import *
from tests import test_header, test_login
from helpers.page_selectors import * # And I done it again
from selenium.common.exceptions import NoSuchElementException

# HELPERS

def add_items_to_cart(driver, items_amount: int) -> None:
    """
    Adds a specified number of items to the cart.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
        items_amount (int): The number of items to add to the cart.

    Raises:
        ValueError: If the requested number of items is greater than the available items or less than or equal to zero.

    Example:
        add_items_to_cart(driver, 3)
    """
    item_buttons = [item["add_to_cart"] for item in ITEMS.values()]

    if not isinstance(items_amount, int):
        raise ValueError(f"Requested items_amount must be an integer, got {type(items_amount).__name__} instead.")

    if items_amount > len(item_buttons) or items_amount <= 0:
        raise ValueError(f"Requested {items_amount} items, but only {len(item_buttons)} items are available.")
    
    for item_button in item_buttons[:items_amount]:
        driver.find_element(*item_button).click()


def validate_cart_badge_display(driver, items_amount: int) -> None:
    """
    Validates that the cart badge is displayed and shows the correct number of items.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
        items_amount (int): The expected number of items in the cart.

    Raises:
        ValueError: If items_amount is not an integer.
        AssertionError: If the cart badge is not displayed or shows incorrect items.

    Example:
        validate_cart_badge_display(driver, 2)
    """
    if not isinstance(items_amount, int):
        raise ValueError("items_amount must be an integer.")

    try:
        cart_badge = driver.find_element(*CART_BADGE)
        assert cart_badge.is_displayed(), "Cart badge is not displayed."
    except NoSuchElementException:
        raise AssertionError("Cart badge element not found.")
    
    assert cart_badge.text == str(items_amount), \
        f"Expected '{items_amount}' in cart, but got '{cart_badge.text}'."


def assert_updated_cart_badge(driver, items_amount) -> None:
    """
    Asserts that the cart badge updates correctly after removing an item.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
        items_amount (int): The current number of items in the cart.

    Raises:
        AssertionError: If the cart badge does not update as expected.

    Example:
        assert_updated_cart_badge(driver, 3)
    """
    driver.find_element(*REMOVE_BACKPACK).click()
    updated_items_amount = items_amount - 1
    if updated_items_amount == 0:
        assert not driver.find_elements(*CART_BADGE), "Cart badge should not be displayed when cart is empty."
    else:
        cart_badge = driver.find_element(*CART_BADGE)
        assert cart_badge.text == str(updated_items_amount), \
            f"Expected '{updated_items_amount}' in cart after removal, but got '{cart_badge.text}'."


def assert_dropdown_options(driver, option_selector) -> None:
    """
    Asserts that a specified option in the dropdown menu is selected.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
        option_selector: The selector for the option to validate.

    Raises:
        AssertionError: If the specified option is not selected.

    Example:
        assert_dropdown_options(driver, (By.XPATH, "//option[@value='asc']"))
    """
    filters_dropdown = driver.find_element(*FILTERS_DRPDWN_MENU)
    filters_dropdown.click()

    driver.find_element(*option_selector).click()

    assert driver.find_element(*option_selector).is_selected(), f"{option_selector} sorting option is not selected."


def assert_sorting_by_value(product_list: list[str], is_descending_order: str, sorting_value: str) -> None:
    """
    Asserts that the product list is sorted by a specified value in the expected order.

    Args:
        product_list (list[str]): The list of products to validate.
        is_descending_order (str): Indicates sorting order ("reverse" for descending).
        sorting_value (str): The attribute by which to sort (e.g., "title").

    Raises:
        AssertionError: If the product list is not sorted as expected.

    Example:
        assert_sorting_by_value(products, "reverse", "price")
    """
    titles = [product[sorting_value] for product in product_list]
    if is_descending_order == "reverse":
        sorted_titles = sorted(titles, reverse=True)
        assert titles == sorted_titles, "The product list is not in Z to A order."
    else:
        sorted_titles = sorted(titles, reverse=False)
        assert titles == sorted_titles, "The product list is not in A to Z order."


def get_items_list(driver) -> list[str]:
    """
    Retrieves a list of products from the product cards on the page.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.

    Returns:
        list[str]: A list of dictionaries containing product details (title, description, price, button).

    Example:
        products = get_items_list(driver)
    """
    # Extract the text from each card and split it into lines
    all_product_cards = driver.find_elements(*ALL_PRODUCT_CARDS)
    products = []

    for card in all_product_cards:
        card_text = card.text.splitlines()
        title = card_text[0]
        description = card_text[1]
        price = float(card_text[2].replace('$', ''))
        button = card_text[3]

        product = {
            "title": title,
            "description": description,
            "price": price,
            "button": button
        }
        products.append(product)

    return products

# TESTS

def test_cart_button_visible(driver):
    test_login.login(driver)
    base_actions.assert_is_element_displayed(driver, CART_BTN)

def test_burger_menu_button_visible(driver):
    test_login.login(driver)
    base_actions.assert_is_element_displayed(driver, BURGER_MENU_BTN)

@pytest.mark.parametrize("items_amount", range(1, 7))
def test_add_all_items_to_cart(driver, items_amount) -> None:
    test_login.login(driver)  
    add_items_to_cart(driver, items_amount)
    validate_cart_badge_display(driver, items_amount)

@pytest.mark.parametrize("items_amount", [0, -1, 8, "str"])  # Testing for invalid cases
def test_add_invalid_items_to_cart(driver, items_amount) -> None:
    test_login.login(driver)  # Log in first if necessary
    with pytest.raises(ValueError, match="Requested"):
        add_items_to_cart(driver, items_amount)

@pytest.mark.parametrize("items_amount", range(1, 7))
def test_updating_cart_badge(driver, items_amount):
    test_login.login(driver)
    add_items_to_cart(driver, items_amount)
    validate_cart_badge_display(driver, items_amount)
    assert_updated_cart_badge(driver, items_amount)

@pytest.mark.parametrize("items_amount", ["str"])  # Testing for invalid value
def test_updating_cart_badge_invalid_value(driver, items_amount):
    test_login.login(driver)
    with pytest.raises(ValueError, match="items_amount"):
        validate_cart_badge_display(driver, items_amount)

@pytest.mark.parametrize("option", SORTING_OPTIONS.keys())
def test_sorting(driver, option):
    option_details = SORTING_OPTIONS[option]
    expected_order = option_details["expected_order"]
    sorting_value = option_details["sorting_value"]
    
    test_login.login(driver)
    assert_dropdown_options(driver, option_details["xpath"])
    products_list = get_items_list(driver)
    assert_sorting_by_value(products_list, expected_order, sorting_value)



