import time
import pytest
from helpers.base_settings import *
from helpers import base_actions
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
        base_actions.assert_is_element_displayed(driver, CHECKOUT_ERROR_CONTATINER)



def fill_checkout_step_1(driver, first_name: str="TestFirstName", last_name: str="TestLastName", zip: str="111"):
    driver.find_element(*FIRST_NAME_INPUT).send_keys(first_name)
    driver.find_element(*LAST_NAME_INPUT).send_keys(last_name)
    driver.find_element(*ZIP_INPUT).send_keys(zip)
    driver.find_element(*CONTINUE_CHECKOUT_BTN).click()


def finish_checkout_assert(driver):
    driver.find_element(*FINISH_BTN).click()
    base_actions.assert_URL(driver, CHECKOUT_COMPLETE_URL)
    base_actions.assert_is_element_displayed(driver, BACK_HOME_BTN)

def cancel_checkout_assert(driver):
    driver.find_element(*CANCEL_BTN).click()
    base_actions.assert_URL(driver, CART_URL)


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
    fill_checkout_step_1(driver)
    checkout_step_1_assert(driver, True)
    finish_checkout_assert(driver)

def test_empty_info_checkout(driver):
    items_amount = 1

    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, items_amount)

    go_to_cart_assert(driver)
    go_to_checkout_1_step_assert(driver)
    fill_checkout_step_1(driver, "", "", "")
    checkout_step_1_assert(driver, False)

@pytest.mark.parametrize("first_name, last_name, zip, expected_error_msg", INVALID_CHECKOUT_INFO_STR)
def test_non_valid_login_checkout(driver, first_name, last_name, zip, expected_error_msg):
    items_amount = 1

    test_login.login(driver)  
    test_main_page.add_items_to_cart(driver, items_amount)

    go_to_cart_assert(driver)
    go_to_checkout_1_step_assert(driver)
    fill_checkout_step_1(driver, first_name, last_name, zip)
    checkout_step_1_assert(driver, False)
    base_actions.assert_element_text(driver, CHECKOUT_ERROR_CONTATINER, expected_error_msg)

def test_checkout_button_visibility(driver):
    items_amount = 1

    test_login.login(driver)
    test_main_page.add_items_to_cart(driver, items_amount)
    
    go_to_cart_assert(driver)
    go_to_checkout_1_step_assert(driver)
    
    base_actions.assert_is_element_displayed(driver, CONTINUE_CHECKOUT_BTN)

def test_cancel_checkout(driver):
    items_amount = 1

    test_login.login(driver)
    test_main_page.add_items_to_cart(driver, items_amount)
    
    go_to_cart_assert(driver)
    go_to_checkout_1_step_assert(driver)
    cancel_checkout_assert(driver)