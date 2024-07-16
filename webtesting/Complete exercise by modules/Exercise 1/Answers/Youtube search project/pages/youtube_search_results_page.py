from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YouTubeSearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.results_container = (By.ID, "contents")
    
    def is_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.results_container)
        )
    
    def get_title(self):
        return self.driver.title
    
    def has_results(self, query):
        results = self.driver.find_elements(By.XPATH, f"//ytd-video-renderer//a[@title[contains(text(), '{query}')]]")
        return len(results) > 0
