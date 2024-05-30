import pytest
from selenium import webdriver


@pytest.fixture
def input_value():
    input_used = 39
    return input_used


@pytest.fixture(scope="function")
def browser():
    """
    Fixture to initialize the browser instance before running each test function.

    Returns:
        WebDriver: Instance of the browser.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(3000)

    env_url = 'https://www.saucedemo.com/'
    driver.get(env_url)

    yield driver

    driver.quit()
