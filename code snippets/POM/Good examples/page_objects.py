from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

class SearchPage:
    def __init__(self, driver):
        self.search_input = (By.NAME, "q")
        self.search_button = (By.NAME, "btnK")

    def enter_search_query(self, query):
        self.driver.find_element(*self.search_input).send_keys(query)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()