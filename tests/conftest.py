import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

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
    """
    browser = request.param
    logging.info(f"Setting up the browser: {browser}")
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
    logging.info(f"Teardown the browser: {browser}")
    driver.quit()

def pytest_html_report_title(report):
    report.title = "Report for Saucedemo"

def pytest_html_results_summary(summary):
    summary.append("<div style='margin-top: 20px;'></div>")
    summary.append("<h2>Test Summary</h2>")

def pytest_html_results_table_row(cells):
    cells[0] = f"<div style='padding: 10px;'>{cells[0]}</div>"
