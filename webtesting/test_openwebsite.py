import pytest
from selenium import webdriver

@pytest.fixture
def browser():
  # Use chromedriver_autoinstaller or manual path as needed
  driver = webdriver.Chrome()
  yield driver
  driver.quit()  # Quit the driver after each test

def test_google_search(browser):
  browser.get("https://www.google.com/")
  assert "Google" in browser.title