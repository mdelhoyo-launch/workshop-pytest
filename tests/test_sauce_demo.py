# Import needed python libraries
import pytest
from selenium import webdriver
from page_objects.pages.sauce_lab_login_page import SauceLabsLoginPage


def test_sauce_demo(browser):
    # Verify when a user is locked out, a “locked out” message will appear

    # Enter username = "locked_out_user"
    sauce_demo_page = SauceLabsLoginPage(browser)
    sauce_demo_page.enter_username('locked_out_user')

    # Enter password = "secret_sauce"
    sauce_demo_page.enter_password('secret_sauce')

    # Click "Login" button
    sauce_demo_page.click_login_button()

    # Verify "locked out" message appears
    assert sauce_demo_page.text_is_on_page('Sorry, this user has been locked out.') is True

    # Close the browser
    browser.quit()


def test_sauce_cart(browser):
    # verify you can add an item to the cart
    # Enter username = "standard_user"
    sauce_demo_page = SauceLabsLoginPage(browser)
    sauce_demo_page.enter_username('standard_user')

    # Enter password = "secret_sauce"
    sauce_demo_page.enter_password('secret_sauce')

    # Click "Login" button
    sauce_demo_page.click_login_button()
