from selenium import webdriver
from enum import Enum
from main.core.utils.logger import CustomLogger


class Browsers(Enum):
    CHROME = "CHROME"
    FIREFOX = "FIREFOX"
    EDGE = "EDGE"


class DriverCreator:
    log = CustomLogger.get_instance()

    @staticmethod
    def create_driver( browser):
        driver = None
        if browser in Browsers:
            if browser == 'CHROME':
                driver = BaseDriver._create_chrome_driver()
            elif browser == 'FIREFOX':
                driver = BaseDriver._create_firefox_driver()
            else:
                driver = BaseDriver._create_edge_driver()
        else:
            BaseDriver.log.warning(f'Invalid browser selected: {browser}')

        return driver

    @staticmethod
    def _create_chrome_driver():
        from chromedriver_py import binary_path
        return webdriver.Chrome(executable_path=binary_path)

    @staticmethod
    def _create_firefox_driver():
        from get_gecko_driver import GetGeckoDriver
        get_driver = GetGeckoDriver()
        get_driver.install()
        return webdriver.Firefox()

    @staticmethod
    def _create_edge_driver():
        import edgedriver_autoinstaller
        edgedriver_autoinstaller.install()
        return webdriver.Edge(executable_path="msedgedriver.exe")
