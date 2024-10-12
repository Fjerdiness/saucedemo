import time
import pytest
from helpers.base_settings import *
from tests import test_login, test_cart
from helpers.page_selectors import * # And I done it again
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def assert_URL(driver, expected_url: str):
    assert driver.current_url == expected_url, \
            f"Expected URL '{expected_url}', but got '{driver.current_url}'"
    
def assert_is_element_displayed(driver, selector):
    element = driver.find_element(*selector)
    assert element.is_displayed(), f"The element with selector {selector} is not visible."

def assert_is_element_invisible(driver, selector):
    try:
        element = driver.find_element(*selector)
        assert not element.is_displayed(), f"The element with selector {selector} is visible, but it should be invisible."
    except NoSuchElementException: # Need to handle NoSuchElementException cos of is_displayed() it will raise an exception if element isnt found
        assert True, f"The element with selector {selector} does not exist, which is expected."



def assert_element_text(driver, selector, expected_text):
    element = driver.find_element(*selector)
    actual_text = element.text
    # print(actual_text) # Debug line
    if actual_text != expected_text:
        raise AssertionError(f"Expected text '{expected_text}', but got '{actual_text}'")

