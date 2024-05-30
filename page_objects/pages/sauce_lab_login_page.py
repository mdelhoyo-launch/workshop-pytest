from page_objects.pages import BasePage
from page_objects.pages.sauce_lab_login_page_locators import SauceLabsLoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class SauceLabsLoginPage(BasePage):
    """Represent SauceLabsLoginPage Actions"""

    def enter_username(self, username: str):
        element = self.wait.until(EC.presence_of_element_located(SauceLabsLoginPageLocators.USERNAME_FIELD))
        element.send_keys(username)

    def enter_password(self, password: str):
        element = self.wait.until(EC.presence_of_element_located(SauceLabsLoginPageLocators.PASSWORD_FIELD))
        element.send_keys(password)

    def click_login_button(self):
        element = self.wait.until(EC.presence_of_element_located(SauceLabsLoginPageLocators.LOGIN_BUTTON))
        element.click()

    def text_is_on_page(self, message: str):
        return message in self.wait.until(EC.presence_of_element_located(SauceLabsLoginPageLocators.BODY)).text
