import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWebAutomation:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://example-login-page.com")
        self.driver.find_element(By.ID, "username").send_keys("myusername")
        self.driver.find_element(By.ID, "password").send_keys("mypassword")
        self.driver.find_element(By.ID, "loginButton").click()
        assert "Dashboard" in self.driver.title

    def test_search(self):
        self.driver.get("http://example-search-page.com")
        self.driver.find_element(By.NAME, "q").send_keys("Selenium")
        self.driver.find_element(By.NAME, "btnK").click()
        assert "Search Results" in self.driver.page_source

if __name__ == "__main__":
    pytest.main()