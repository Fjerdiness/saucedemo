import pytest
from helpers.base_settings import *
from tests import base_actions
from helpers.page_selectors import * # And I done it again
from tests import test_login, test_main_page

# HELPERS

def go_to_cart_assert(driver):
    driver.find_element(*CART_BTN).click()
    base_actions.assert_URL(driver, CART_URL)
    
def continue_shopping_click_assert(driver):
    driver.find_element(*CONTINUE_SHOPPING_BTN).click()
    base_actions.assert_URL(driver, INVENTORY_URL)

def go_to_checkout_1_step_assert(driver):
    driver.find_element(*CHECKOUT_BTN).click()
    base_actions.assert_URL(driver, CHECKOUT_1_URL)

def checkout_step_1_assert(driver, is_valid: bool):
    if is_valid:
        base_actions.assert_URL(driver, CHECKOUT_2_URL)
    else: 
        assert driver.find_element(*CHECKOUT_ERROR_CONTATINER).is_displayed(), "Checkout error should be visible"

def fill_checkout_step_1(driver, first_name, last_name, zip):
    driver.find_element(*FIRST_NAME_INPUT).send_keys(first_name)
    driver.find_element(*LAST_NAME_INPUT).send_keys(last_name)
    driver.find_element(*ZIP_INPUT).send_keys(zip)
    driver.find_element(*CONTINUE_CHECKOUT_BTN).click()


def finish_checkout_assert(driver):
    driver.find_element(*FINISH_BTN).click()
    base_actions.assert_URL(driver, CHECKOUT_COMPLETE_URL)
    assert driver.find_element(*BACK_HOME_BTN).is_displayed(), "Back Home button isnt displayed"

def cancel_checkout_assert(driver):
    driver.find_element(*CANCEL_BTN).click()
    current_url = driver.current_url
    assert current_url == INVENTORY_URL, f"Expected URL '{INVENTORY_URL}', but got '{current_url}'."

def assert_checkout_btn_is_not_visible():
    assert CHECKOUT_BTN.is_displayed(), "Checkout button is not visible."


# TESTS

def test_go_to_cart(driver):
    items_amount = 1

    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, items_amount)

    go_to_cart_assert(driver)

def test_continue_shopping_click(driver):
    items_amount = 1

    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, items_amount)

    go_to_cart_assert(driver)
    continue_shopping_click_assert(driver)

def test_valid_checkout(driver):
    items_amount = 1

    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, items_amount)

    go_to_cart_assert(driver)
    go_to_checkout_1_step_assert(driver)
    fill_checkout_step_1(driver, "Test", "Est", 123)
    checkout_step_1_assert(driver, True)
    finish_checkout_assert(driver)

def test_non_valid_checkout(driver):
    items_amount = 1

    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, items_amount)

    go_to_cart_assert(driver)
    go_to_checkout_1_step_assert(driver)
    fill_checkout_step_1(driver, "", "", "")
    checkout_step_1_assert(driver, False)

def test_checkout_button_visibility(driver):
    items_amount = 1

    test_login.login(driver)
    test_main_page.add_items_to_cart(driver, items_amount)
    
    go_to_cart_assert(driver)
    go_to_checkout_1_step_assert(driver)
    
    assert_checkout_btn_is_not_visible()

def test_cancel_checkout(driver):
    items_amount = 1

    test_login.login(driver)
    test_main_page.add_items_to_cart(driver, items_amount)
    
    go_to_cart_assert(driver)
    go_to_checkout_1_step_assert(driver)
    cancel_checkout_assert(driver)