import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode."
    )

@pytest.fixture(params=["chrome", "edge", "firefox"])
def driver(request):
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
