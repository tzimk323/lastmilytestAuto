from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest


class Navbar2(BasePage):
    projectsPageButton: WebElement

    driver: WebDriver

    locators = {
        'projectsPageButton': ('id', "projectsPageButton"),
    }

    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""

    def waitPageVisible(self):
        pass

    #TODO :change the id

    def isPageDisplayed(self):
        pass

    def clickProjectButton(self):
        self.projectsPageButton.click()
