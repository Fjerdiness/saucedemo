from helpers.base_settings import *
from helpers.page_selectors import * # And I done it again
from selenium.common.exceptions import NoSuchElementException

def assert_URL(driver, expected_url: str) -> None:
    """
    Assert that the current URL of the driver matches the expected URL.

    Args:
        driver: The WebDriver instance controlling the browser.
        expected_url (str): The URL expected to be the current URL of the driver.

    Raises:
        AssertionError: If the current URL does not match the expected URL.
    """
    assert driver.current_url == expected_url, \
        f"Expected URL '{expected_url}', but got '{driver.current_url}'"

def assert_is_element_displayed(driver, selector: Tuple[By, str]) -> None:
    """
    Assert that a specific element is displayed in the browser.

    Args:
        driver: The WebDriver instance controlling the browser.
        selector (Tuple[By, str]): A tuple containing the method to locate the element and its identifier.

    Raises:
        AssertionError: If the element is not displayed.
    """
    element = driver.find_element(*selector)
    assert element.is_displayed(), f"The element with selector {selector} is not visible."

def assert_is_element_invisible(driver, selector: Tuple[By, str]) -> None:
    """
    Assert that a specific element is not visible in the browser.

    Args:
        driver: The WebDriver instance controlling the browser.
        selector (Tuple[By, str]): A tuple containing the method to locate the element and its identifier.

    Raises:
        AssertionError: If the element is visible when it is expected to be invisible.
    """
    try:
        element = driver.find_element(*selector)
        assert not element.is_displayed(), f"The element with selector {selector} is visible, but it should be invisible."
    except NoSuchElementException:
        pass

def assert_element_text(driver, selector: Tuple[By, str], expected_text: str) -> None:
    """
    Assert that the text of a specific element matches the expected text.

    Args:
        driver: The WebDriver instance controlling the browser.
        selector (Tuple[By, str]): A tuple containing the method to locate the element and its identifier.
        expected_text (str): The text expected to match the element's text.

    Raises:
        AssertionError: If the actual text does not match the expected text.
    """
    element = driver.find_element(*selector)
    actual_text = element.text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"

def get_element_text(driver, selector: Tuple[By, str]) -> str:
    """
    Retrieve the text of a specific element.

    Args:
        driver: The WebDriver instance controlling the browser.
        selector (Tuple[By, str]): A tuple containing the method to locate the element and its identifier.

    Returns:
        str: The text content of the specified element.
    """
    element = driver.find_element(*selector)
    return element.text

    

