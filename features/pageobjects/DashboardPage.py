import cdp.tracing
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest

from selenium import webdriver


class DashboardPage(BasePage):

    shipmentsChart: WebElement
    driver: WebDriver

    locators = {
        'shipmentsChart': ('id', "shipments-chart"),

    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.shipmentsChart.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get("shipmentsChart"))

        # self.waitElementDisplayed(self.locators.get('newProjectButton'))


