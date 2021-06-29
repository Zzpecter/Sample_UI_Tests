from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.chrome.webdriver import WebDriver
from main.automationpractice.pages.buttons_page import ButtonsPage
from main.automationpractice.webdriver_factory.driver_creator import DriverCreator
from main.core.utils.file_reader import read_json

scenarios('../features')


@fixture()
def browser():
    #TODO: test the json decoding
    browser_to_use = read_json('../../config.json').get('browser')
    _browser = WebDriver()
    _browser.implicitly_wait(15)
    _browser.maximize_window()
    yield _browser
    _browser.close()
    _browser.quit()


@given(parsers.parse('I want to test the "{page}" section'))
def try_section(browser, page):
    if page == 'Buttons':
        ButtonsPage(browser).open()


@when("I click on a button")
def click_on_button(browser):
    ButtonsPage(browser).click_left()


@then(parsers.parse('I should see a confirmation message'))
def validate_message(browser):
    result_text = ButtonsPage(browser).get_popup_left()
    assert result_text == ''

