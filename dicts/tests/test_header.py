import time
import pytest
from base_settings import *
from tests import test_login, test_cart
from page_selectors import * # And I done it again
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# HELPERS
def assert_burger_menu_buttons_visibility(driver):
    driver.find_element(*BURGER_MENU_BTN).click()  
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((BURGER_MENU_SUBBTNS["All Items"]))
    )
    for button_name, button_selector in BURGER_MENU_SUBBTNS.items():
        assert driver.find_element(*button_selector).is_displayed(), f"{button_name} button is not visible."

def click_burger_menu_option(driver, *button_selector):
    driver.find_element(*BURGER_MENU_BTN).click()  
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((BURGER_MENU_SUBBTNS["All Items"]))
    )
    
    driver.find_element(*button_selector).click()

# TESTS

def test_burger_menu_buttons_visibility(driver):
    test_login.login(driver) 
    assert_burger_menu_buttons_visibility(driver)

def test_burger_menu_items_click(driver):
    test_login.login(driver)
    test_cart.assert_cart_page_opened(driver)
    click_burger_menu_option(driver, *BURGER_MENU_SUBBTNS["All Items"])
    