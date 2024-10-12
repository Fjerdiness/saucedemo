
import time
import pytest
from helpers import base_actions
from helpers.base_settings import *
from tests import test_login
from helpers.page_selectors import * # And I done it again
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

def assert_updated_cart_badge(driver, items_amount) -> None:
    driver.find_element(*REMOVE_BACKPACK).click()
    updated_items_amount = items_amount - 1
    if updated_items_amount == 0:
            assert not driver.find_elements(*CART_BADGE), "Cart badge should not be displayed when cart is empty."
    else:
        cart_badge = driver.find_element(*CART_BADGE)
        assert cart_badge.text == str(updated_items_amount), \
            f"Expected '{updated_items_amount}' in cart after removal, but got '{cart_badge.text}'."

def check_dropdown_assert_values(driver) -> None:
    filters_dropdown = driver.find_element(*FILTERS_DRPDWN_MENU)
    assert filters_dropdown.is_displayed(), "Filters dropdown is not visible."

    for option_name, option_selector in DROPDOWN_MENU_OPTIONS.items():
        filters_dropdown.click()  
        assert driver.find_element(*option_selector).is_displayed(), f"{option_name} sorting option is not visible."
        driver.find_element(*option_selector).click()  
        filters_dropdown = driver.find_element(*FILTERS_DRPDWN_MENU)
        assert driver.find_element(*option_selector).is_selected(), f"{option_name} sorting option is not selected."

def select_dropdown_option_assert(driver, option_selector) -> None:
    filters_dropdown = driver.find_element(*FILTERS_DRPDWN_MENU)
    filters_dropdown.click()

    driver.find_element(*option_selector).click()

    assert driver.find_element(*option_selector).is_selected(), f"{option_selector} sorting option is not selected."

def assert_ordering_by_letters(product_list:list[str], is_descending_order:bool) -> None:
    titles = [product['title'] for product in product_list]
    if is_descending_order: 
        sorted_titles = sorted(titles, reverse=True)
        assert titles == sorted_titles, "The product list is not in Z to A order."
    else: 
        sorted_titles = sorted(titles, reverse=False)
        assert titles == sorted_titles, "The product list is not in A to Z order."
    
def assert_ordering_by_price(product_list:list[str], is_descending_order:bool) -> None:
    prices = [float(product['price'].replace('$', '')) for product in product_list]
    if is_descending_order: 
        sorted_titles = sorted(prices, reverse=True)
        assert prices == sorted_titles, "The product list is not in Low to High pricing order."
    else: 
        sorted_titles = sorted(prices, reverse=False)
        assert prices == sorted_titles, "The product list is not in High to Low pricing order."

def get_items_list(driver) -> list[str]:
    # Extract the text from each card and split it into lines

    all_product_cards = driver.find_elements(*ALL_PRODUCT_CARDS)
    products = [] 

    for card in all_product_cards:
        card_text = card.text.splitlines()
        
        if len(card_text) >= 4:
            title = card_text[0]
            description = card_text[1]
            price = card_text[2]
            button = card_text[3]

            product = {
                "title": title,
                "description": description,
                "price": price,
                "button": button
            }
            products.append(product)

    # for product in products:
    #     print(product) # debug lines

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

def test_sorting_by_letter_reverse(driver):
    test_login.login(driver)
    select_dropdown_option_assert(driver, DROPDOWN_MENU_OPTIONS["Z to A"])
    products_list = get_items_list(driver)
    assert_ordering_by_letters(products_list, True)

def test_sorting_by_letter(driver):
    test_login.login(driver)
    select_dropdown_option_assert(driver, DROPDOWN_MENU_OPTIONS["Z to A"])
    products_list = get_items_list(driver)
    assert_ordering_by_letters(products_list, True)
    select_dropdown_option_assert(driver, DROPDOWN_MENU_OPTIONS["A to Z"])
    products_list = get_items_list(driver)
    assert_ordering_by_letters(products_list, False)

def test_sorting_by_price_reverse(driver):
    test_login.login(driver)
    select_dropdown_option_assert(driver, DROPDOWN_MENU_OPTIONS["Low to High"])
    products_list = get_items_list(driver)
    assert_ordering_by_price(products_list, False)

def test_sorting_by_price(driver):
    test_login.login(driver)
    select_dropdown_option_assert(driver, DROPDOWN_MENU_OPTIONS["High to Low"])
    products_list = get_items_list(driver)
    assert_ordering_by_price(products_list, True)


