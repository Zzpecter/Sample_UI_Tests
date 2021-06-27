from __future__ import unicode_literals, print_function
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

from main.core.utils.logger import CustomLogger
from main.gui.utils.constants import SUPPORTED_BROWSERS, BASE_URL


class Webdriver():


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
            print('URL did not launch successfully.')

        return self.driver

    def getBytype(self, locator):
        if locator == 'id':
            return By.ID

        if locator == 'name':
            return By.NAME

        if locator == 'class':
            return By.CLASS_NAME

        if locator == 'link-text':
            return By.LINK_TEXT

        if locator == 'xpath':
            return By.XPATH

        if locator == 'css':
            return By.CSS_SELECTOR

        if locator == 'tag':
            return By.TAG_NAME


    def getElement(self, locator, locatortype):
        locator = self.getBytype(locator)
        wait = WebDriverWait(self.driver, 10)
        #element = self.driver.find_element(locator, locatortype)
        try:
            elementCheck = wait.until(EC.element_to_be_clickable((locator, locatortype)))
            if elementCheck is not None:
                print("#"*30)
                print("Element with locators '{0}{1}{2}' found successfully".format(locator, ",", locatortype))
                #elementCheck.click()
                return elementCheck
            else:
                print("#" * 30)
                print("Element '{0}' is not present".format(locator + locatortype))
        except:
            print("Not able to find element")

        return self.driver

    def close(self):
        self.driver.close()
