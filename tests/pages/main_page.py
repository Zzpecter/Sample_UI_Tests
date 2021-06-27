from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from main.gui.utils.constants import BASE_URL
from main.gui.webdriver import WebDriver


class MainPage:
    checkbox_locator = (By.LINK_TEXT, "checkboxes")

    def __init__(self, browser):
        self.browser = browser
        self._url = BASE_URL
        self.driver = WebDriver()

    def load(self):
        self.browser.get(self._url)

    def click_checkboxes(self):
        cb_element = self.browser.find_element(*self.checkbox_locator)
        ActionChains(self.driver).click(cb_element)
