import pytest
from helpers.base_settings import * # Yeah, I know I shouldnt do this, but i did
from helpers.page_selectors import *
from helpers import base_actions
from selenium.common.exceptions import WebDriverException
    
# HELPERS    

def login(driver, username: str = "standard_user", password: str = "secret_sauce") -> None:
    """
    Logs in to the application using the provided username and password.

    This function navigates to the base URL, fills in the login form, and submits it.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
        username (str): The username to log in with. Defaults to "standard_user".
        password (str): The password to log in with. Defaults to "secret_sauce".

    Raises:
        WebDriverException: If there is an error during the login process.

    Example:
        login(driver, "my_username", "my_password")
    """
    try:
        driver.get(BASE_URL)
        driver.find_element(*USERNAME_INPUT).send_keys(username)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BTN).click()
    except WebDriverException as e:
        print(f"Encountered an error: {e}")
        raise

        
# TESTS 

@pytest.mark.parametrize("username,password", VALID_CREDS.items())
def test_valid_login(driver, username, password):
    login(driver, username, password)
    base_actions.assert_URL(driver, INVENTORY_URL)
    base_actions.assert_is_element_displayed(driver, HEADER_LOGO)

def test_no_username_login(driver):
    login(driver, username="")
    base_actions.assert_is_element_displayed(driver, LOGIN_ERROR_CONTAINER)
    base_actions.assert_element_text(driver, LOGIN_ERROR_CONTAINER, LOGIN_ERRORS_STR[0])

def test_no_password_login(driver):
    login(driver, password="")
    base_actions.assert_is_element_displayed(driver, LOGIN_ERROR_CONTAINER)
    base_actions.assert_element_text(driver, LOGIN_ERROR_CONTAINER, LOGIN_ERRORS_STR[1])

@pytest.mark.parametrize("username,password", NON_VALID_CREDS.items())    
def test_locked_out_user_login(driver, username, password):
    login(driver, username, password)
    base_actions.assert_is_element_displayed(driver, LOGIN_ERROR_CONTAINER)
    base_actions.assert_element_text(driver, LOGIN_ERROR_CONTAINER, LOGIN_ERRORS_STR[2])

def test_non_existent_login(driver):
    login(driver, username="a", password="a")
    base_actions.assert_is_element_displayed(driver, LOGIN_ERROR_CONTAINER)
    base_actions.assert_element_text(driver, LOGIN_ERROR_CONTAINER, LOGIN_ERRORS_STR[3])

def test_login_webdriver_exception(driver, monkeypatch):  # Simulate a WebDriverException
    def mock_get(url):
        raise WebDriverException("Simulated WebDriver exception.")
    
    monkeypatch.setattr(driver, 'get', mock_get)

    with pytest.raises(WebDriverException, match="Simulated WebDriver exception."):
        login(driver)



