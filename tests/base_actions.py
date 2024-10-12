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
    
def is_element_displayed(driver, button):
    button_element = driver.find_element(*button)
    assert button_element.is_displayed(), f"The element with selector {button} is not visible."