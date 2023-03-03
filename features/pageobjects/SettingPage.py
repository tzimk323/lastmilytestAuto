import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest


class SettingsPage(BasePage):
    # Navigation list
    timeWindowsSection: WebElement
    navigationList: WebElement
    chargesSection: WebElement


    # charges section
    timeWindowsSection: WebElement

    driver: WebDriver

    locators = {
        'timeWindowsSection': ('id', "time-windows"),
        'navigationList': ('id', "navigation-list"),
        'chargesSection': ('id', "charges"),
    }

    newZoneChargeButton: WebElement
    locators.update(newZoneChargeButton =('id', "new_zone_charge"))

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.navigationList.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get('navigationList'))

    def waitTimeWindowsSectionDisplayed(self):
        self.waitElementDisplayed(self.locators.get('timeWindowsSection'))

    def waitChargesSectionDisplayed(self):
        self.waitElementDisplayed(self.locators.get('chargesSection'))

    def scrollIntoViewToSection(self,section):
        if section == 'time windows':
            ActionChains(self.driver).scroll_to_element(self.timeWindowsSection)
            self.waitElementDisplayed(self.timeWindowsSection)
        elif(section == 'charges'):
            ActionChains(self.driver).scroll_to_element(self.chargesSection)
            self.waitChargesSectionDisplayed()

    def clickInsettingsMenuToVisitSection(self, section):
        optionList=self.navigationList.find_elements(By.CSS_SELECTOR,"li[class='section-link']")
        if section == 'time windows':
            ref = "time-windows"
        elif (section == 'charges'):
            ref = "charges"
        self.navigationList.find_element(By.CSS_SELECTOR, f"a[ref='{ref}']").click()
        self.waitPageToLoad()
        self.waitPageToLoad() # time.sleep(2)

    def clickNewZoneChargesButton(self):
        self.newZoneChargeButton.click()




    """Page Actions"""
