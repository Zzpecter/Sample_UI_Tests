import os
from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.pages.main_page import MainPage
from tests.pages.buttons_page import ButtonsPage

scenarios('features')


@fixture()
def browser():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    _browser = WebDriver(os.path.join(dir_path, "chromedriver.exe"))
    yield _browser
    _browser.close()
    _browser.quit()


@given(parsers.parse('I want to test the "{section}" section'))
def test_section(browser, section):
    if section == 'Buttons':
        ButtonsPage(browser).load()


@when("I click on a buttons")
def click_on_button(browser):
    ButtonsPage(browser).click_left()


@then(parsers.parse('I should see a confirmation message'))
def validate_message(browser, text):
    result_text = ButtonsPage(browser).get_popup_left()
    assert result_text == 'Close'

