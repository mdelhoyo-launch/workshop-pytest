from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
