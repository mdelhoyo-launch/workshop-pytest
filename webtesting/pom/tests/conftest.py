import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Can change path to your WebDriver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()