import pytest
from helpers.base_settings import *
from helpers import base_actions
from helpers.page_selectors import * # And I done it again
from tests import test_header, test_login, test_main_page


ITEMS_AMOUNT = 1

# HELPERS

def assert_cart_page_opened(driver) -> None:
    """
    Asserts that the cart page is opened by clicking the cart button.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
    
    Example:
        assert_cart_page_opened(driver)
    """
    driver.find_element(*CART_BTN).click()
    base_actions.assert_URL(driver, CART_URL)


def continue_shopping_click_assert(driver) -> None:
    """
    Clicks the continue shopping button and asserts that the inventory page is opened.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
    
    Example:
        continue_shopping_click_assert(driver)
    """
    driver.find_element(*CONTINUE_SHOPPING_BTN).click()
    base_actions.assert_URL(driver, INVENTORY_URL)


def go_to_checkout_1_step_assert(driver) -> None:
    """
    Clicks the checkout button and asserts that the first checkout step page is opened.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
    
    Example:
        go_to_checkout_1_step_assert(driver)
    """
    driver.find_element(*CHECKOUT_BTN).click()
    base_actions.assert_URL(driver, CHECKOUT_1_URL)


def checkout_step_1_assert(driver, is_valid: bool) -> None:
    """
    Asserts the result of the first checkout step.

    If `is_valid` is True, it asserts that the second checkout step page is opened.
    If `is_valid` is False, it asserts that the checkout error container is displayed.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
        is_valid (bool): Indicates whether the checkout step is valid or not.

    Example:
        checkout_step_1_assert(driver, True)
    """
    if is_valid:
        base_actions.assert_URL(driver, CHECKOUT_2_URL)
    else: 
        base_actions.assert_is_element_displayed(driver, CHECKOUT_ERROR_CONTATINER)


def fill_checkout_step_1(driver, first_name: str = "TestFirstName", last_name: str = "TestLastName", zip: str = "111") -> None:
    """
    Fills in the first step of the checkout process with provided customer details.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
        first_name (str): The customer's first name. Defaults to "TestFirstName".
        last_name (str): The customer's last name. Defaults to "TestLastName".
        zip (str): The customer's zip code. Defaults to "111".

    Example:
        fill_checkout_step_1(driver, "John", "Doe", "12345")
    """
    driver.find_element(*FIRST_NAME_INPUT).send_keys(first_name)
    driver.find_element(*LAST_NAME_INPUT).send_keys(last_name)
    driver.find_element(*ZIP_INPUT).send_keys(zip)
    driver.find_element(*CONTINUE_CHECKOUT_BTN).click()


def finish_checkout_assert(driver) -> None:
    """
    Clicks the finish button and asserts that the checkout completion page is opened.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.

    Example:
        finish_checkout_assert(driver)
    """
    driver.find_element(*FINISH_BTN).click()
    base_actions.assert_URL(driver, CHECKOUT_COMPLETE_URL)
    base_actions.assert_is_element_displayed(driver, BACK_HOME_BTN)


def cancel_checkout_assert(driver) -> None:
    """
    Clicks the cancel button and asserts that the cart page is reopened.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.

    Example:
        cancel_checkout_assert(driver)
    """
    driver.find_element(*CANCEL_BTN).click()
    base_actions.assert_URL(driver, CART_URL)


# TESTS

def test_go_to_cart(driver):
    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, ITEMS_AMOUNT)

    assert_cart_page_opened(driver)

def test_continue_shopping_click(driver):    
    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, ITEMS_AMOUNT)

    assert_cart_page_opened(driver)
    continue_shopping_click_assert(driver)

def test_valid_checkout(driver):
    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, ITEMS_AMOUNT)

    assert_cart_page_opened(driver)
    go_to_checkout_1_step_assert(driver)
    fill_checkout_step_1(driver)
    checkout_step_1_assert(driver, True)
    finish_checkout_assert(driver)

def test_empty_info_checkout(driver):
    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, ITEMS_AMOUNT)

    assert_cart_page_opened(driver)
    go_to_checkout_1_step_assert(driver)
    fill_checkout_step_1(driver, "", "", "")
    checkout_step_1_assert(driver, False)

@pytest.mark.parametrize("first_name, last_name, zip, expected_error_msg", INVALID_CHECKOUT_INFO_STR)
def test_non_valid_checkout(driver, first_name, last_name, zip, expected_error_msg):
    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, ITEMS_AMOUNT)

    assert_cart_page_opened(driver)
    go_to_checkout_1_step_assert(driver)
    fill_checkout_step_1(driver, first_name, last_name, zip)
    checkout_step_1_assert(driver, False)
    base_actions.assert_element_text(driver, CHECKOUT_ERROR_CONTATINER, expected_error_msg)

def test_checkout_button_visibility(driver):
    test_login.login(driver)
    test_main_page.add_items_to_cart(driver, ITEMS_AMOUNT)
    
    assert_cart_page_opened(driver)
    go_to_checkout_1_step_assert(driver)
    
    base_actions.assert_is_element_displayed(driver, CONTINUE_CHECKOUT_BTN)

def test_cancel_checkout(driver):
    test_login.login(driver)
    test_main_page.add_items_to_cart(driver, ITEMS_AMOUNT)
    
    assert_cart_page_opened(driver)
    go_to_checkout_1_step_assert(driver)
    cancel_checkout_assert(driver)

def test_cart_persistence(driver):
    test_login.login(driver)
    test_main_page.add_items_to_cart(driver, ITEMS_AMOUNT)
    inital_cart_value = base_actions.get_element_text(driver, CART_BADGE)
    test_header.click_burger_menu_option(driver, *BURGER_MENU_SUBBTNS["Logout"])
    base_actions.assert_URL(driver, BASE_URL)
    test_login.login(driver)
    cart_value = base_actions.get_element_text(driver, CART_BADGE)
    assert inital_cart_value == cart_value, f"Test failed, expected {inital_cart_value}, but got {cart_value}"
