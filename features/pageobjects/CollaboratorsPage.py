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


class CollaboratorsPage(BasePage):
    locators = {}
    driver: WebDriver

    newCollaboratorButton: WebElement
    locators.update(newCollaboratorButton=('id', "new-collaborator-button"))

    collaboratorsBar: WebElement
    locators.update(collaboratorsBar=('id', "white-bar"))

    rightClickList: WebElement
    locators.update(rightClickList=('xpath', ".//div[@class='H_context_menu H_el']"))

    # NewPartnersModal
    newCollaboratorsNameField: WebElement
    locators.update(newCollaboratorsNameField=('id', "name-customer-collaborators-form"))

    newCollaboratorsAddressField: WebElement
    locators.update(newCollaboratorsAddressField=('id', "address-customer-collaborators-form"))

    newCollaboratorsMap: WebElement
    locators.update(newCollaboratorsMap=('id', "collaborator-map"))

    newCollaboratorsTaxIDField: WebElement
    locators.update(newCollaboratorsTaxIDField=('id', "tax-id-customer-collaborators-form"))

    newCollaboratorsTaxofficeField: WebElement
    locators.update(newCollaboratorsTaxofficeField=('id', "tax-office-customer-collaborators-form"))

    newCollaboratorsEmailField: WebElement
    locators.update(newCollaboratorsEmailField=('id', "email-customer-collaborators-form"))

    newCollaboratorsDeportAddressField: WebElement
    locators.update(newCollaboratorsDeportAddressField=('id', "depot-address-customer-collaborators-form"))

    inviteNewCollaboratorsButton: WebElement
    locators.update(inviteNewCollaboratorsButton=('id', "invite_collaborator_button"))

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.newCollaboratorButton.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators.get("newCollaboratorButton"))
        self.waitPageToLoad()  # time.sleep(2)
        time.sleep(1)

    def waitNewCollaboratorModalVisible(self):
        self.waitElementDisplayed(self.locators.get("newCollaboratorsNameField"))
        self.waitPageToLoad()

    def waitNewCollaboratorsModalNOTVisible(self):
        self.waitElementNotDisplayed(self.locators.get("newCollaboratorsNameField"))
        self.waitPageToLoad()

    def chooseCollaboratorWithName(self,name):
        # rows = self.driver.find_element(By.CSS_SELECTOR, "div[class='ag-center-cols-clipper']").find_elements(By.XPATH,".//div[@class='ag-center-cols-container']/div")
        # for line in cells:
        #     column = line.find_element(By.CSS_SELECTOR, "div[aria-colindex='1']")
        #     if column.text.split("\n")[1] == name:
        #         column.click()

        cells = self.driver.find_elements(By.CSS_SELECTOR, "div[role='gridcell']")

        for gridcell in cells:
            if name in gridcell.text:
                gridcell.click()
                break


    """Page Actions"""

    def iClickNewCollaboratorsButton(self):
        self.newCollaboratorButton.click()

    def iSetNewCollaboratorsNameToBe(self, name):
        self.setTextField(self.newCollaboratorsNameField, name)

    def iSetNewCollaboratorsDepotAddressTobe(self, address):
        self.chooseDropDownTab(self.newCollaboratorsDeportAddressField, address)

    def iSetNewCollaboratorsTaxIDToBe(self, taxid):
        self.setTextField(self.newCollaboratorsTaxIDField, taxid)

    def iSetNewCollaboratorsTaxOfficeToBe(self, office):
        self.setTextField(self.newCollaboratorsTaxofficeField, office)

    def iSetNewCollaboratorsEmailAddressTobe(self, email):
        self.setTextField(self.newCollaboratorsEmailField, email)

    def iSetNewCollaboratorsAddressTobe(self, address):
        self.chooseDropDownTab(self.newCollaboratorsAddressField, address)

    def rightClickOnMapAndChoose(self, option, x, y):
        ActionChains(self.driver).move_to_element_with_offset(self.newCollaboratorsMap, x, y).perform()
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

    def iSetNewCollaboratorsAddressByClickingOnMap(self):
        self.rightClickOnMapAndChoose("Διεύθυνση", 0, 170)

    def iSetNewCollaboratorsDepotAddressByClickingOnMap(self):
        self.rightClickOnMapAndChoose("Διεύθυνση Αποθήκης", 0, 150)

    def iClickNewCollaboratorsSubmitButton(self):
        self.inviteNewCollaboratorsButton.click()
