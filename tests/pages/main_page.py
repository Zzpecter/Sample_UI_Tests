from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from main.gui.utils.constants import BASE_URL
from main.gui.webdriver import WebDriver

_CONTACT_PAGE_LOCATOR = (By.ID, "contact-us")
_BUTTONS_PAGE_LOCATOR = (By.ID, "button-clicks")
_LOGIN_PAGE_LOCATOR = (By.ID, "login-portal")
_SELECTORS_PAGE_LOCATOR = (By.ID, "dropdown-checkboxes-radiobuttons")
_ACTIONS_PAGE_LOCATOR = (By.ID, "actions")


class MainPage:

    def __init__(self, browser):
        self.browser = browser
        self._url = BASE_URL
        self.driver = WebDriver().driver

    def load(self):
        self.browser.get(self._url)

    def click_contact(self):
        contact_element = self.browser.find_element(_CONTACT_PAGE_LOCATOR)
        ActionChains(self.driver).click(contact_element)

    def click_buttons(self):
        buttons_element = self.browser.find_element(_BUTTONS_PAGE_LOCATOR)
        ActionChains(self.driver).click(buttons_element)

    def click_login(self):
        login_element = self.browser.find_element(_LOGIN_PAGE_LOCATOR)
        ActionChains(self.driver).click(login_element)

    def click_selectors(self):
        selectors_element = self.browser.find_element(_SELECTORS_PAGE_LOCATOR)
        ActionChains(self.driver).click(selectors_element)

    def click_actions(self):
        actions_element = self.browser.find_element(_ACTIONS_PAGE_LOCATOR)
        ActionChains(self.driver).click(actions_element)
