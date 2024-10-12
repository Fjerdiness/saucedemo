import pytest
from selenium import webdriver
from helpers.base_settings import * # Yeah, I know I shouldnt do this, but i did
from helpers.page_selectors import *
from selenium.common.exceptions import NoSuchElementException
from tests import base_actions
    
# HELPERS    

def login(driver, username: str="standard_user", password: str="secret_sauce"):
    driver.get(BASE_URL)
    driver.find_element(*USERNAME_INPUT).send_keys(username)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BTN).click()

# TESTS 

@pytest.mark.parametrize("username,password", VALID_CREDS.items())
def test_valid_login(driver, username, password):
    login(driver, username, password)
    base_actions.assert_URL(driver, INVENTORY_URL)
    base_actions.is_element_displayed(driver, HEADER_LOGO)

@pytest.mark.parametrize("username,password", NON_VALID_CREDS.items())    
def test_locked_out_login(driver, username, password):
    login(driver, username, password)
    try:
        error_container = driver.find_element(*LOGIN_ERROR_CONTAINER)
        assert error_container.is_displayed(), "Error message is not displayed as expected."
    except NoSuchElementException:
        assert False, "Error message container does not exist."
