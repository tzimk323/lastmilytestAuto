import time

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


class ZoneChargesPage(BasePage):
    locators = {}
    driver: WebDriver

    zoneNameField: WebElement
    locators.update(zoneNameField=('id', "zone-name-field"))

    zoneChargesSubmit: WebElement
    locators.update(zoneChargesSubmit=('id', "sumbit-zone-charges-button"))

    zoneChargesCloseButton: WebElement
    locators.update(zoneChargesCloseButton=('id', "close_zone_charges"))

    newWeightChargesButton: WebElement
    locators.update(newWeightChargesButton=('id', "new-weight-charges"))

    newItemChargesButton: WebElement
    locators.update(newItemChargesButton=('id', "new-item-charges"))

    newServicesChargesButton: WebElement
    locators.update(newServicesChargesButton=('id', "new-services-charges"))

    newServicesChadfhrgesButton: WebElement
    locators.update(newServicesChargesButton=('id', "new-services-charges"))




    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.zoneChargesSubmit.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get("zoneChargesSubmit"))
        self.waitPageToLoad() # time.sleep(2)



    """Page Actions"""

    def iSetZoneChargesName(self, name):
        self.setTextField(self.zoneNameField,name)

    def iClickAddNewWeightCharge(self):
        self.newWeightChargesButton.click()

        # ///////////////////////////////////////////////////WeightModal/////////////////////////////////////////////////////////

    weightChargeModal: WebElement
    locators.update(weightChargeModal=('id', "weight-charges-modal"))

    weightCloseModal: WebElement
    locators.update(weightCloseModal=('id', "weight-close-modal"))

    weightDropDown: WebElement
    locators.update(weightDropDown=('id', "weight-confines-dropdown"))

    weightChargesCrowd: WebElement
    locators.update(weightChargesCrowd=('id', "weight-charges-from-form"))

    weightChargesMeter: WebElement
    locators.update(weightChargesMeter=('id', "weight-charges-meter"))

    weightChargesAmountField: WebElement
    locators.update(weightChargesAmountField=('id', "weight-charges-amount-form"))

    weightModalSubmitButton: WebElement
    locators.update(weightModalSubmitButton=('id', "weight-modal-submit"))


    def iClickZoneChargesSubmitButton(self):
        self.zoneChargesSubmit.click()

    def iClickWeightModalSubmitButton(self):
        self.weightModalSubmitButton.click()

    def setWeightChargesNumber(self,number):
        self.setTextField(self.weightChargesCrowd,number)

    def setWeightChargesAmount(self,amount):
        self.setTextField(self.weightChargesAmountField,amount)

    def chooseWeightChargesFromToDropDown(self,FromTo):
        self.chooseDropDown(self.weightDropDown,FromTo)

    def chooseWeightChargesMeterDropDown(self,amount):
        self.chooseDropDown(self.weightChargesMeter, amount)

    def waitWeighChargeModalDisplayed(self):
        self.waitElementDisplayed(self.locators.get("weightChargeModal"))
        self.waitPageToLoad() # time.sleep(2)

    def waitWeighChargeModalNOTDisplayed(self):
        self.waitElementNotDisplayed(self.locators.get("weightChargeModal"))
        self.waitPageToLoad() # time.sleep(2)