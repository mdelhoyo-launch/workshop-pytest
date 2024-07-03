from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")

    def open(self):
        self.driver.get("https://www.google.com")

    def search(self, query):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
