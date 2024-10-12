
import time
import pytest
from helpers.base_settings import *
from tests import test_login, base_actions
from helpers.page_selectors import * # And I done it again
from selenium.common.exceptions import NoSuchElementException

# HELPERS

def add_items_to_cart(driver, items_amount: int) -> None:
    item_buttons = [item["add_to_cart"] for item in ITEMS.values()]

    if items_amount > len(item_buttons) or items_amount <= 0:
        raise ValueError(f"Requested {items_amount} items, but only {len(item_buttons)} items are available.")
    
    for item_button in item_buttons[:items_amount]:
        driver.find_element(*item_button).click()


def assert_cart_badge(driver, items_amount: int) -> None:
    try:
        cart_badge = driver.find_element(*CART_BADGE)
    except NoSuchElementException:
        pass  # This is the expected behavior  
    assert cart_badge.is_displayed(), "Cart badge is not displayed."
    assert cart_badge.text == str(items_amount), \
        f"Expected '{items_amount}' in cart, but got '{cart_badge.text}'."

def assert_updated_cart_badge(driver, items_amount):
    driver.find_element(*REMOVE_BACKPACK).click()
    updated_items_amount = items_amount - 1
    if updated_items_amount == 0:
            assert not driver.find_elements(*CART_BADGE), "Cart badge should not be displayed when cart is empty."
    else:
        cart_badge = driver.find_element(*CART_BADGE)
        assert cart_badge.text == str(updated_items_amount), \
            f"Expected '{updated_items_amount}' in cart after removal, but got '{cart_badge.text}'."

def check_dropdown_assert_values(driver):
    filters_dropdown = driver.find_element(*FILTERS_DRPDWN_MENU)
    assert filters_dropdown.is_displayed(), "Filters dropdown is not visible."

    for option_name, option_selector in DROPDOWN_MENU_OPTIONS.items():
        filters_dropdown.click()  
        assert driver.find_element(*option_selector).is_displayed(), f"{option_name} sorting option is not visible."
        driver.find_element(*option_selector).click()  
        filters_dropdown = driver.find_element(*FILTERS_DRPDWN_MENU)
        assert driver.find_element(*option_selector).is_selected(), f"{option_name} sorting option is not selected."


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
    assert_cart_badge(driver, items_amount)

@pytest.mark.parametrize("items_amount", range(1, 7))
def test_updating_cart_badge(driver, items_amount):
    test_login.login(driver)
    add_items_to_cart(driver, items_amount)
    assert_cart_badge(driver, items_amount)
    assert_updated_cart_badge(driver, items_amount)


def test_filters_dropdown_visibility(driver):
    items_amount = 1

    test_login.login(driver)
    add_items_to_cart(driver, items_amount)
    check_dropdown_assert_values(driver)









