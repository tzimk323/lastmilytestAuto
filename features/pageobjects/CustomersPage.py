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

from selenium import webdriver


class CustomersPage(BasePage):
    locators = {}
    driver: WebDriver

    map: WebElement
    locators.update(map=('id', "map"))
    newCustomerButton: WebElement
    locators.update(newCustomerButton=('id', "new-customer-button"))

    customerNameField: WebElement
    locators.update(customerNameField=('id', "name-customer-form"))

    customerNewAddress: WebElement
    locators.update(customerNewAddress=('id', "custom-input-customer-form"))

    customerPhoneField: WebElement
    locators.update(customerPhoneField=('id', "telephone-customer-form"))

    newCustomerModal: WebElement
    locators.update(newCustomerModal=('xpath', ".//div[@class='customer-modal side-modal open']"))





    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.newCustomerButton.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get("newCustomerButton"))
        # self.waitPageToLoad() # time.sleep(2)



    """Page Actions"""

    def iClickNewCustomerButton(self):
        self.newCustomerButton.click()

    def waitNewCustomerPageDisplayed(self):
        self.waitElementDisplayed(self.locators.get("customerNameField"))
        # self.waitPageToLoad() # time.sleep(2)

    def waitNewCustomerPageNotDisplayed(self):
        self.waitElementNotDisplayed(self.locators.get("customerNameField"))
        # self.waitPageToLoad() # time.sleep(2)



    def setNewCustomerAddress(self,address):
        self.chooseDropDownType(self.customerNewAddress,address)

    def setNewCustomerAddressByMapClick(self):
        ActionChains(self.driver).move_to_element(self.map).perform()
        ActionChains(self.driver).context_click().perform()
        time.sleep(2)


    def setNewCustomerPhoneNumber(self,number):
        self.setTextField(self.customerPhoneField,number)

    def setNewCustomerName(self,name):
        self.setTextField(self.customerNameField,name)

    def clickNewCustomerModalSubmitButton(self):
        self.newCustomerModal.find_element(By.CSS_SELECTOR,"button[class='waves-effect waves-light btn-large modal-button flex-1']").click()
