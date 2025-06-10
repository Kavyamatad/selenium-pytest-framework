import pytest
from Pages.Login_page import LoginPage
from Utils.config_reader import get_default
from Utils.logger import setup_logger

logger = setup_logger()


def test_login_with_ini_credentials(driver):
    logger.info("Test started: test_login_with_ini_credentials")
    login_page = LoginPage(driver)
    username = get_default("username")
    password = get_default("password")
    login_page.login(username, password)

    actual_url = driver.current_url
    expected_substring = "inventory"
    assert expected_substring in actual_url, f"Login failed, current URL: {actual_url}"
    logger.info("Login successful. Reached inventory page.")