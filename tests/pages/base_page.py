from selenium.webdriver.chrome import webdriver
from main.gui.utils.constants import BASE_URL


class BasePage(object):
    url_path = None

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, **kwargs):
        url = "/".join([BASE_URL, self.url_path])
        url = url.format(kwargs)
        return url

    def open(self, **kwargs):
        self.driver.get(self.get_url(**kwargs))
        return self

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _find_all(self, locator):
        return self.driver.find_elements(*locator)

    def _type(self, locator, text):
        text_area = self._find(locator)
        text_area.clear()
        text_area.send_keys(text)
        return self
