from __future__ import unicode_literals, print_function
from selenium import webdriver

from main.core.utils.logger import CustomLogger
from main.gui.utils.constants import SUPPORTED_BROWSERS, BASE_URL


class WebDriver:
    def __init__(self, driver):
        self.logger = CustomLogger(name='gui-logger')
        self.driver = driver

    def launch_browser(self, browser_type):

        assert browser_type in SUPPORTED_BROWSERS
        if browser_type == 'edge':
            self.driver = webdriver.Edge()

        elif browser_type == 'firefox':
            self.driver = webdriver.Firefox()

        elif browser_type == 'chrome':
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        if self.driver.title is not None:
            self.logger.info(f'URL {BASE_URL} Launched, '
                             f'Title of the page: {self.driver.title}.')
        else:
            self.logger.info('URL did not launch successfully.')

        return self.driver

    def get_element(self, locator):
        pass

    def close(self):
        self.driver.close()
