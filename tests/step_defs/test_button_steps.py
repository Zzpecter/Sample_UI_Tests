import os
from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.pages.main_page import MainPage
from tests.pages.buttons_page import ButtonsPage
from main.core.utils.logger import CustomLogger

scenarios('../features')


@fixture()
def browser():
    _browser = WebDriver()
    yield _browser
    _browser.close()
    _browser.quit()


@given(parsers.parse('I want to test the "{section}" section'))
def test_section(browser, section):
    ButtonsPage(browser).open()


@when("I click on a button")
def click_on_button(browser):
    ButtonsPage(browser).click_left()


@then(parsers.parse('I should see a confirmation message'))
def validate_message(browser):
    result_text = ButtonsPage(browser).get_popup_left()
    assert result_text == 'Close'

