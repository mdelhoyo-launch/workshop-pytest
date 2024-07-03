from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleSearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_results = (By.ID, "search")

    def is_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_results)
        )

    def get_title(self):
        return self.driver.title

    def has_results(self, query):
        results = self.driver.find_elements(By.XPATH, f"//span[contains(text(), '{query}')]")
        return len(results) > 0
