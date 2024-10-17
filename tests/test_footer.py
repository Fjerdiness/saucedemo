import time
from helpers.base_settings import *
from helpers.page_selectors import * # And I done it again
from tests import test_login
from helpers import base_actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# HELPERS

def social_network_click_assert(driver, button: Tuple[By, str], expected_url:str):
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

    

