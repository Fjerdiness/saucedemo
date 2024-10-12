from helpers import base_actions
from helpers.base_settings import *
from tests import test_login, test_cart
from helpers.page_selectors import * # And I done it again
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

# HELPERS
def check_burger_menu_buttons_visibility(driver) -> None:
    driver.find_element(*BURGER_MENU_BTN).click()  
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located((BURGER_MENU_SUBBTNS["All Items"]))
    )
    for button_name, button_selector in BURGER_MENU_SUBBTNS.items():
        assert driver.find_element(*button_selector).is_displayed(), f"{button_name} button is not visible."

def click_burger_menu_option(driver, *button_selector) -> None:
    driver.find_element(*BURGER_MENU_BTN).click()  
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.visibility_of_element_located((BURGER_MENU_SUBBTNS["All Items"])) # Waiting till burger menu animation
    )
    
    driver.find_element(*button_selector).click()

# TESTS

def test_burger_menu_buttons_visibility(driver):
    test_login.login(driver) 
    check_burger_menu_buttons_visibility(driver)

def test_burger_menu_all_items_click(driver):
    test_login.login(driver)
    test_cart.assert_cart_page_opened(driver)
    click_burger_menu_option(driver, *BURGER_MENU_SUBBTNS["All Items"])
    base_actions.assert_URL(driver, INVENTORY_URL)

def test_burger_menu_about_click(driver):
    test_login.login(driver)
    click_burger_menu_option(driver, *BURGER_MENU_SUBBTNS["About"])
    base_actions.assert_URL(driver, SAUCELABS_URL)

def test_burger_menu_logout_click(driver):
    test_login.login(driver)
    click_burger_menu_option(driver, *BURGER_MENU_SUBBTNS["Logout"])
    base_actions.assert_URL(driver, BASE_URL)

def test_burger_menu_reset_app_click(driver):
    test_login.login(driver)
    click_burger_menu_option(driver, *BURGER_MENU_SUBBTNS["Reset App State"])
    base_actions.assert_is_element_invisible(driver, CART_BADGE)
    
