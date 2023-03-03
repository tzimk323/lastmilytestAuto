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


class CollaboratorPartnerView(BasePage):
    locators = {}
    driver: WebDriver

    collaboratorNavBar: WebElement
    locators.update(collaboratorNavBar=('id', "white-bar"))

    collaboratorName: WebElement
    locators.update(collaboratorName=('xpath', ".//div[@class='collaborator-name']"))

    stopPointCount: WebElement
    locators.update(stopPointCount=('xpath', ".//div[@class='stop-points-count-container']"))

    allPointsFilterButton: WebElement
    locators.update(allPointsFilterButton=('xpath', ".//div[@class='filter-type-box-container'][1]"))

    historyPointsFilterButton: WebElement
    locators.update(historyPointsFilterButton=('xpath', ".//div[@class='filter-type-box-container'][2]"))

    paymentOnDeliveryPointsFilterButton: WebElement
    locators.update(paymentOnDeliveryPointsFilterButton=('xpath', ".//div[@class='filter-type-box-container'][3]"))

    invoicePointsFilterButton: WebElement
    locators.update(invoicePointsFilterButton=('xpath', ".//div[@class='filter-type-box-container'][4]"))

    invoicePartnerPointsFilterButton: WebElement
    locators.update(invoicePartnerPointsFilterButton=('xpath', ".//div[@class='filter-type-box-container'][5]"))

    customerName: WebElement
    locators.update(customerName=('xpath', ".//div[@class='customer-name']"))

    manualInvoicingButton: WebElement
    locators.update(manualInvoicingButton=('id', "manual-invoicing-button"))

    invoiceButton: WebElement
    locators.update(invoiceButton=('xpath', ".//div[@id='invoice-action-button']/button"))

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.collaboratorName.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get("collaboratorName"))
        self.waitPageToLoad()  # time.sleep(2)

    def waitPartnerPageVisible(self):
        self.waitElementDisplayed(self.locators.get("customerName"))
        self.waitPageToLoad()
    def waitCollaboratorPartnerPageVisible(self):
        self.waitElementDisplayed(self.locators.get("stopPointCount"))
        self.waitPageToLoad()

    def waitCollaboratorViewStopPointPageVisible(self):
        self.waitElementDisplayed(self.locators.get("stopPointCount"))

        self.waitPageToLoad()  # time.sleep(2)

    def iChooseFromCollaboratorViewNavbarOptionWithOrder(self, option):
        navbuttons = self.collaboratorNavBar.find_elements(By.XPATH, "div")
        counter = 0
        for button in navbuttons:
            counter += 1
            if counter == option:
                button.click()

    def iChooseCollaboratorFilterInvoiceButton(self):
        self.invoicePointsFilterButton.click()

    def iChoosePartnerFilterInvoiceButton(self):
        self.invoicePartnerPointsFilterButton.click()

    def iChooseColaboratorPartnerManualInvoiceButton(self):
        self.manualInvoicingButton.click()

    def iCheckForInvoiceTheStopPointWithCreationDate(self,creationDate):
        cells = self.driver.find_elements(By.CSS_SELECTOR, "div[role='gridcell']")
        for gridcell in cells:
            if gridcell.text.split("\n")[0] == creationDate:
                gridcell.find_element(By.XPATH,"..").find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
                time.sleep(1)
                break
    def iCheckForInvoiceTheStopPointWithAddress(self,address):
        cells = self.driver.find_elements(By.CSS_SELECTOR, "div[role='gridcell']")
        for gridcell in cells:
            if gridcell.text.replace("\n"," ") == address:
                gridcell.find_element(By.XPATH,"..").find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
                time.sleep(1)
                break


    def getFromInvoiceElementsCellNumber(self, row, column):
        return self.driver.find_element(By.CSS_SELECTOR, "div[class='ag-center-cols-clipper']").find_element(
            By.CSS_SELECTOR, f"div[aria-rowindex='{int(row) + 1}']").find_element(By.CSS_SELECTOR,
                                                                                  f"div[aria-colindex='{int(column)}']").text

    def iclickFromInvoiceNumberTheActionButton(self,row):
        return self.driver.find_element(By.CSS_SELECTOR, "div[class='ag-center-cols-clipper']").find_element(
            By.CSS_SELECTOR, f"div[aria-rowindex='{int(row) + 1}']").find_element(By.CSS_SELECTOR,
                                                                                  "button[class='invoices-actions-button approve-button']").click()

    def iclickInvoiceButton(self):
        self.invoiceButton.click()

