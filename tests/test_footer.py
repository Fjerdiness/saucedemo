import time
from helpers.base_settings import *
from helpers.page_selectors import * # And I done it again
from tests import test_login
from helpers import base_actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# HELPERS

def social_network_click_assert(driver, button: Tuple[By, str], expected_url:str):
    """
    Clicks a social network button, waits for the new page to load,
    and asserts that the current URL contains the expected URL.

    This function performs the following steps:
    1. Clicks the specified button to open a new window.
    2. Switches to the newly opened window.
    3. Waits until the URL of the new page contains the expected substring.
    4. Asserts that the current URL matches the expected criteria.
    5. Closes the new window and switches back to the original window.

    Args:
        driver (webdriver): The Selenium WebDriver instance used to control the browser.
        button (Tuple[By, str]): A tuple containing the strategy to locate the button and its identifier.
        expected_url (str): The expected substring that should be present in the current URL.

    Raises:
        AssertionError: If the current URL does not contain the expected substring.

    Example:
        social_network_click_assert(driver, (By.ID, "link-to-social"), "expected-url-part")
    """
    driver.find_element(*button).click()
    driver.switch_to.window(driver.window_handles[-1]) # Switch to the new window
    WebDriverWait(driver, 10).until(
        EC.url_contains(expected_url)  # Wait until the URL contains the expected substring
    )
    assert expected_url in driver.current_url, f"Expected URL to contain '{expected_url}', but got '{driver.current_url}'." # God I hate linkedin for that 
    driver.close()
    driver.switch_to.window(driver.window_handles[0]) # Switch back to the original window

# TESTS


def test_social_media_links(driver):
    test_login.login(driver)  

    social_network_click_assert(driver, XITTER_BTN, XITTER_URL)  
    social_network_click_assert(driver, FB_BTN, FB_URL)  
    social_network_click_assert(driver, LINKEDIN_BTN, LINKEDIN_URL)  

    

