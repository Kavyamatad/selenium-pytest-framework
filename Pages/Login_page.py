# pages/login_page.py
import time

from selenium.webdriver.common.by import By
from Utils.csv_loader import load_locators
from Utils.logger import setup_logger

logger = setup_logger()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = load_locators()

    def login(self, username, password):
        logger.info("Starting login process")
        self.driver.find_element(By.XPATH, self.locators["username"]).send_keys(username)
        logger.info("Entered username")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.locators["password"]).send_keys(password)
        logger.info("Entered password")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.locators["login"]).click()
        logger.info("Clicked login button")
        time.sleep(3)