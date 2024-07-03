import pytest
from selenium import webdriver
from page_objects import LoginPage, SearchPage

class TestWebAutomation:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://example-login-page.com")
        login_page = LoginPage(self.driver)
        login_page.enter_username("myusername")
        login_page.enter_password("mypassword")
        login_page.click_login()
        assert "Dashboard" in self.driver.title

    def test_search(self):
        self.driver.get("http://example-search-page.com")
        search_page = SearchPage(self.driver)
        search_page.enter_search_query("Selenium")
        search_page.click_search()
        assert "Search Results" in self.driver.page_source

if __name__ == "__main__":
    pytest.main()