import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(executable_path='./drivers/chromedriver')  # Update path to your WebDriver OR remove the argument to remain default
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def pytest_html_report_title(report):
    report.title = "YouTube Search Test Report"

def pytest_configure(config):
    config._metadata['Project Name'] = 'YouTube Search'
    config._metadata['Tester'] = 'Your Name'
