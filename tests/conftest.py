import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    """
    Adds command-line options for pytest.

    Args:
        parser: The pytest parser instance used to add options.

    This function adds an option to run tests in headless mode.
    Example usage:
        pytest --headless
    """
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode."
    )


@pytest.fixture(params=["chrome", "edge", "firefox"])
def driver(request):
    """
    Provides a Selenium WebDriver instance for testing.

    Args:
        request: The pytest request object that provides access to test parameters.

    Yields:
        webdriver: A Selenium WebDriver instance configured for the specified browser.

    This fixture supports Chrome, Edge, and Firefox, and can run in headless mode if specified.
    Example usage:
        def test_example(driver):
            driver.get("http://example.com")
    """
    browser = request.param
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        service = EdgeService()
        driver = webdriver.Edge(service=service, options=options)
    
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError("Unsupported browser")

    yield driver
    driver.quit()

