from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    def __init__(self, driver webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)