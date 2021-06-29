from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from main.automationpractice.pages.base_page import BasePage


class MainPage(BasePage):

    url_path = ""
    _CONTACT_PAGE_LOCATOR = (By.ID, "contact-us")
    _BUTTONS_PAGE_LOCATOR = (By.ID, "button-clicks")
    _LOGIN_PAGE_LOCATOR = (By.ID, "login-portal")
    _SELECTORS_PAGE_LOCATOR = (By.ID, "dropdown-checkboxes-radiobuttons")
    _ACTIONS_PAGE_LOCATOR = (By.ID, "actions")

    def __init__(self, driver):
        super().__init__(driver)

    def click_contact(self):
        contact_element = self.browser.find_element(self._CONTACT_PAGE_LOCATOR)
        ActionChains(self.driver).click(contact_element)

    def click_buttons(self):
        buttons_element = self.browser.find_element(self._BUTTONS_PAGE_LOCATOR)
        ActionChains(self.driver).click(buttons_element)

    def click_login(self):
        login_element = self.browser.find_element(self._LOGIN_PAGE_LOCATOR)
        ActionChains(self.driver).click(login_element)

    def click_selectors(self):
        selectors_element = self.browser.find_element(self._SELECTORS_PAGE_LOCATOR)
        ActionChains(self.driver).click(selectors_element)

    def click_actions(self):
        actions_element = self.browser.find_element(self._ACTIONS_PAGE_LOCATOR)
        ActionChains(self.driver).click(actions_element)
