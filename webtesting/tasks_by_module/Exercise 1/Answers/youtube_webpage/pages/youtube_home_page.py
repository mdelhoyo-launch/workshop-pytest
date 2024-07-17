from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YouTubeHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "search_query")
    
    def open(self):
        self.driver.get("https://www.youtube.com")
    
    def search(self, query):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
