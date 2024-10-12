import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "edge"]) # Was doing this on Windows machine, thus Edge and not Safari, just as a PoC
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()
