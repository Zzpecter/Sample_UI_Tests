from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from main.gui.utils.constants import BASE_URL, BUTTONS_PAGE_URL
from main.gui.webdriver import WebDriver

_BUTTON_LEFT_LOCATOR = (By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/div[2]/span/p")
_BUTTON_MIDDLE_LOCATOR = (By.CSS_SELECTOR, "#button2")
_BUTTON_RIGHT_LOCATOR = (By.ID, "button3")
_BUTTON_HOME_LOCATOR = (By.CSS_SELECTOR, "#nav-title")
_BUTTON_CLOSE_LOCATOR = (By.CSS_SELECTOR, ".modal-md > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")


class ButtonsPage:

    def __init__(self, browser):
        self.browser = browser
        self._url = BASE_URL + BUTTONS_PAGE_URL
        self.driver = WebDriver()

    def load(self):
        self.browser.get(self._url)

    def click_left(self):
        button_element = self.browser.find_element(_BUTTON_LEFT_LOCATOR)
        return ActionChains(self.driver).click(button_element)

    def click_middle(self):
        button_element = self.browser.find_element(_BUTTON_MIDDLE_LOCATOR)
        return self.driver.driver.execute_script("arguments[0].click();", button_element)

    def click_right(self):
        button_element = self.browser.find_element(_BUTTON_RIGHT_LOCATOR)
        return ActionChains(self.driver).click(button_element)

    def click_home(self):
        button_element = self.browser.find_element(_BUTTON_HOME_LOCATOR)
        return ActionChains(self.driver.driver).move_to_element(button_element).click(button_element)

    def get_popup_left(self):
        popup_element = self.browser.find_element(_BUTTON_CLOSE_LOCATOR)
        return popup_element.text
