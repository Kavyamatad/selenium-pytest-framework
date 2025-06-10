import pytest
from selenium import webdriver
from Utils.config_reader import get_default

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=get_default("browser"), help="Browser to use")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    url = get_default("base_url")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Unsupported browser")

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
