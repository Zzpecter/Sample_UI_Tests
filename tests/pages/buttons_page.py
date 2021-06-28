from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from main.gui.utils.constants import BASE_URL, BUTTONS_PAGE_URL
from tests.pages.base_page import BasePage


class ButtonsPage(BasePage):
    url_path = BUTTONS_PAGE_URL
    _BUTTON_LEFT_LOCATOR = (By.XPATH, "//span[@id='button1']")
    _BUTTON_MIDDLE_LOCATOR = (By.CSS_SELECTOR, "div.container div.caption #button2")
    _BUTTON_RIGHT_LOCATOR = (By.ID, "button3")
    _BUTTON_HOME_LOCATOR = (By.CSS_SELECTOR, "#nav-title")
    _BUTTON_CLOSE_LOCATOR = (By.CSS_SELECTOR, ".modal-md > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)")

    def __init__(self, driver):
        super().__init__(driver)

    def click_left(self):
        button_element = self._find(self._BUTTON_LEFT_LOCATOR)
        return ActionChains(self.driver).click(button_element)

    def click_middle(self):
        button_element = self._find(self._BUTTON_MIDDLE_LOCATOR)
        return self.driver.execute_script("arguments[0].click();", button_element)

    def click_right(self):
        button_element = self._find(self._BUTTON_RIGHT_LOCATOR)
        return ActionChains(self.driver).click(button_element)

    def click_home(self):
        button_element = self._find(self._BUTTON_HOME_LOCATOR)
        return ActionChains(self.driver.driver).move_to_element(button_element).click(button_element)

    def get_popup_left(self):
        popup_element = self._find(self._BUTTON_CLOSE_LOCATOR)
        return popup_element.text
