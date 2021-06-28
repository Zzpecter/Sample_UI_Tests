from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.pages.buttons_page import ButtonsPage

scenarios('../features')


@fixture()
def browser():
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

