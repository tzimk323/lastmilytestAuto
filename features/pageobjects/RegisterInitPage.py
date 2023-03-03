from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest


class RegisterInitPage(BasePage):
    #    Locators

    startDemoButton: WebElement
    startCompanyButton: WebElement

    driver: WebDriver

    locators = {
        'startDemoButton': ('id', 'startDemo'),
        'startCompanyButton': ('id', 'startCompany')
    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.startDemoButton.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators['startDemoButton'])

    def clickstartCompanyButton(self):
        self.startCompanyButton.click()

    def isStartCompanyButtonDisplayed(self):
        return self.startCompanyButton.is_displayed()

    def isStartDemoButtonDisplayed(self):
        return self.startDemoButton.is_displayed()
