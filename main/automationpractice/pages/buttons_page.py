from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from main.ui.utils.constants import BUTTONS_PAGE_URL
from main.automationpractice.pages.base_page import BasePage
from main.core.utils.logger import CustomLogger


class ButtonsPage(BasePage):
    url_path = BUTTONS_PAGE_URL
    _BUTTON_LEFT_LOCATOR = (By.XPATH, "//span[@id='button1']")
    _BUTTON_MIDDLE_LOCATOR = (By.CSS_SELECTOR, "div.container div.caption #button2")
    _BUTTON_RIGHT_LOCATOR = (By.ID, "button3")
    _BUTTON_HOME_LOCATOR = (By.CSS_SELECTOR, "#nav-title")
    _BUTTON_CLOSE_LOCATOR = (By.CSS_SELECTOR, "#myModalClick > div > div > div.modal-footer > button")

    def __init__(self, driver):
        super().__init__(driver)
        self.log = CustomLogger('ui-logger')

    def click_left(self):
        button_element = self._find(self._BUTTON_LEFT_LOCATOR)
        self.log.info(f'Found Element: {button_element}')
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
        self.log.info(f'Popup Element: {popup_element}')
        return popup_element.text
