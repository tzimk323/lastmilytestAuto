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


class PartnersPage(BasePage):
    locators = {}
    driver: WebDriver

    newPartnerButton: WebElement
    locators.update(newPartnerButton=('id', "new-button"))

    partnersBar: WebElement
    locators.update(partnersBar=('id', "white-bar"))

    rightClickList: WebElement
    locators.update(rightClickList=('xpath', ".//div[@class='H_context_menu H_el']"))

    # NewPartnersModal
    newPartnersNameField: WebElement
    locators.update(newPartnersNameField=('id', "name-customer-collaborators-form"))

    newPartnersAddressField: WebElement
    locators.update(newPartnersAddressField=('id', "address-customer-collaborators-form"))

    newPartnersMap: WebElement
    locators.update(newPartnersMap=('id', "collaborator-map"))

    newPartnersTaxIDField: WebElement
    locators.update(newPartnersTaxIDField=('id', "tax-id-customer-collaborators-form"))

    newPartnersTaxofficeField: WebElement
    locators.update(newPartnersTaxofficeField=('id', "tax-office-customer-collaborators-form"))

    newPartnersEmailField: WebElement
    locators.update(newPartnersEmailField=('id', "email-customer-collaborators-form"))

    inviteNewParntnerButton: WebElement
    locators.update(inviteNewParntnerButton=('id', "invite_partner_button"))

    # PARTNERS NAVBAR

    collaboratorOverviewButton: WebElement
    locators.update(collaboratorOverviewButton=('xpath', ".//div[@routerlink='collaboratorOverview']"))

    newShipmentsViewButton: WebElement
    locators.update(newShipmentsViewButton=('xpath', ".//div[@routerlink='newShipmentsView']"))

    shipmentsHistoryButton: WebElement
    locators.update(shipmentsHistoryButton=('xpath', ".//div[@routerlink='shipmentsHistory'][2]"))

    viewPartnerButton: WebElement
    locators.update(viewPartnerButton=('xpath', ".//div[@routerlink='partners']"))

    filtersContainer: WebElement
    locators.update(filtersContainer=('id', "filters-container"))


    balanceContainer: WebElement
    locators.update(balanceContainer=('id', "balance-container"))







    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.newPartnerButton.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get("newPartnerButton"))
        self.waitPageToLoad() # time.sleep(2)
        time.sleep(1)

    def waitNewPartnerModalVisible(self):
        self.waitElementDisplayed(self.locators.get("newPartnersNameField"))
        self.waitPageToLoad()

    def waitNewPartnerModalNOTVisible(self):
        self.waitElementNotDisplayed(self.locators.get("newPartnersNameField"))
        self.waitPageToLoad()

    """Page Actions"""
    def iClickNewPartnersButton(self):
        self.newPartnerButton.click()

    def iClickShipmentsHistoryButton(self):
        self.shipmentsHistoryButton.click()

    def iClickViewPartnersButton(self):
        self.viewPartnerButton.click()

    def waitShipmentsHistoryPageDisplayed(self):
        self.waitElementDisplayed(self.locators['filtersContainer'])

    def waitViewPartnersPageDisplayed(self):
        self.waitElementDisplayed(self.locators['balanceContainer'])


    # Start at 1
    def getFromShipmentHistoryNumberElementCellNumber(self,row,column):
        return self.driver.find_element(By.CSS_SELECTOR,"div[class='ag-center-cols-clipper']").find_element(By.CSS_SELECTOR,f"div[aria-rowindex='{int(row)+1}']").find_element(By.CSS_SELECTOR,f"div[aria-colindex='{int(column)}']").text

    def iSetNewPartnerNameToBe(self,name):
        self.setTextField(self.newPartnersNameField,name)

    def iSetNewPartnerTaxIDToBe(self,taxid):
        self.setTextField(self.newPartnersTaxIDField,taxid)

    def iSetNewPartnerTaxOfficeToBe(self,office):
        self.setTextField(self.newPartnersTaxofficeField,office)

    def iSetNewPartnerEmailAddressTobe(self,email):
        self.setTextField(self.newPartnersEmailField,email)

    def iSetNewPartnerAddressTobe(self, address):
        self.chooseDropDownTab(self.newPartnersAddressField, address)


    def iSetNewPartnerAddressFromMapClick(self):
        self.rightClickOnMapAndChoose("Διεύθυνση", 40, 170)


    def choosePartnerWithName(self,name):
        rows= self.driver.find_element(By.CSS_SELECTOR, "div[class='ag-center-cols-clipper']").find_elements(By.XPATH, ".//div[@class='ag-center-cols-container']/div")
        for line in rows:
            column=line.find_element(By.CSS_SELECTOR,"div[aria-colindex='1']")
            if column.text.split("\n")[1] == name:
                column.click()




    def rightClickOnMapAndChoose(self, option, x, y):
        ActionChains(self.driver).move_to_element_with_offset(self.newPartnersMap, x, y).perform()
        ActionChains(self.driver).context_click().perform()
        self.waitElementDisplayed(self.locators['rightClickList'])
        elements = self.rightClickList.find_elements(By.XPATH, "div")
        selected = False
        for choices in elements:
            if choices.text.lower() == option.lower():
                ActionChains(self.driver).move_to_element(choices).perform()
                choices.click()
                selected = True
                break;
        if not selected:
            raise Exception("Right click choice on collaborators map does not exist")
        self.waitPageToLoad()  # time.sleep(2)


    def iClickNewPartnerSubmitButton(self):
        self.inviteNewParntnerButton.click()