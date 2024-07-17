import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Can change path to your WebDriver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def pytest_html_report_title(report):
    report.title = "Search Test Report"

def pytest_configure(config):
    config._metadata['Project Name'] = 'Web Search'
    config._metadata['Tester'] = 'Your Name here'