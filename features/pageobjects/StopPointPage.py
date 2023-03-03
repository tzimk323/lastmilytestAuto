import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest


class StopPointPage(BasePage):
    locators = {}
    driver: WebDriver



    recipientMap: WebElement
    locators.update(recipientMap=('id', "recipient-map"))

    collaboratorNameField: WebElement
    locators.update(collaboratorNameField=('id', "collaborator-name-voucher-form"))

    # Locators
    voucherOption: WebElement
    locators.update(voucherOption=('id', "voucher_option"))
    noVoucherOption: WebElement
    locators.update(noVoucherOption=('id', "no_voucher_option"))
    submitVoucherButton: WebElement
    locators.update(submitVoucherButton=('id', "submit-voucher-button-buffer"))
    deliveryVoucherRadio: WebElement
    locators.update(deliveryVoucherRadio=('id', "delivery_voucher_radio"))
    pickupVoucherRadio: WebElement
    locators.update(pickupVoucherRadio=('id', "pickup_voucher_radio"))
    samedayVoucherRadio: WebElement
    locators.update(samedayVoucherRadio=('id', "sameday_voucher_radio"))

    # Sender
    weightCloseModal: WebElement
    locators.update(weightCloseModal=('id', "weight-close-modal"))
    senderCompanyRadio: WebElement
    locators.update(senderCompanyRadio=('id', "radio-collaborator-company"))
    senderPersonRadio: WebElement
    locators.update(senderPersonRadio=('id', "radio-collaborator-person"))
    senderNameField: WebElement
    locators.update(senderNameField=('id', "collaborator-name-voucher-form"))
    senderAdrressField: WebElement
    locators.update(senderAdrressField=('id', "sender-address-custom-input"))
    senderCountryPrefixList: WebElement
    locators.update(senderCountryPrefixList=('id', "country-code-dropdown"))
    senderPhoneField: WebElement
    locators.update(senderPhoneField=('id', "sender-telephone-voucher-form"))
    senderDepotField: WebElement
    locators.update(senderDepotField=('id', "depot-start-end"))
    senderDriversList: WebElement
    locators.update(senderDriversList=('id', "assign-to-drivers-cover"))
    senderDriversSelection: WebElement
    locators.update(senderDriversSelection=('id', "assign-to-drivers-cover"))

    byOrderCheckbox: WebElement
    locators.update(byOrderCheckbox=('xpath', "//input[@formcontrolname='thirdPartyCheckboxSelected']"))

    # if by order
    cosignorNameField: WebElement
    locators.update(cosignorNameField=('id', "consignor-name-voucher-form"))



    # if receive in sender
    senderNoDeliveryCheckbox: WebElement
    locators.update(senderNoDeliveryCheckbox=('id', "no_deliver_checkbox"))
    pickupTimeWindowSlider: WebElement
    locators.update(pickupTimeWindowSlider=('id', "pickup_time_window_slider"))
    pickupDurationSlider: WebElement
    locators.update(pickupDurationSlider=('id', "pickup_duration_slider"))
    pickupClientPortalToggle: WebElement
    locators.update(pickupClientPortalToggle=('id', "pickup_clientp_toggle"))
    pickupPriorityToggle: WebElement
    locators.update(pickupPriorityToggle=('id', "pickup_priority_toggle"))

    # Receiver
    recipientNameField: WebElement
    locators.update(recipientNameField=('id', "recipient-name-voucher-form"))
    recipientAddressField: WebElement
    locators.update(recipientAddressField=('id', "recipient-address-custom-input"))
    recipientCountryPrefix: WebElement
    locators.update(recipientCountryPrefix=('id', "recipient-country-code"))
    recipientPhoneField: WebElement
    locators.update(recipientPhoneField=('id', "telephone-voucher-form"))
    recipientAgreedDate: WebElement
    locators.update(recipientAgreedDate=('id', "agreed-shipping-date-voucher"))
    recipientDurationSlider: WebElement
    locators.update(recipientDurationSlider=('id', "recipient-duration-slider"))
    recipientTimeWindowDoubleSlider: WebElement
    locators.update(recipientTimeWindowDoubleSlider=('id', "time-window-double-slider"))
    recipientEnabledToggle: WebElement
    locators.update(recipientEnabledToggle=('id', "enabled_toggle"))
    recipientPortalToggle: WebElement
    locators.update(recipientPortalToggle=('id', "portal_toggle"))
    recipientPriorityToggle: WebElement
    locators.update(recipientPriorityToggle=('id', "priority_toggle"))

    # Charges
    chargeTypeList: WebElement
    locators.update(chargeTypeList=('id', "type-of-charge"))
    chargeAmountField: WebElement
    locators.update(chargeAmountField=('id', "pay-amount-voucher-form"))
    chargeCardCheckbox: WebElement
    locators.update(chargeCardCheckbox=('id', "card-checkbox"))
    chargeChargeZoneList: WebElement
    locators.update(chargeChargeZoneList=('id', "zone-of-charge-options"))
    chargeServicesCharge: WebElement
    locators.update(chargeServicesCharge=('id', "services-charge"))
    chargeVolumeCategoryList: WebElement
    locators.update(chargeVolumeCategoryList=('id', "volume-category"))
    chargeHeightField: WebElement
    locators.update(chargeHeightField=('id', "height-voucher-form"))
    chargeWidthField: WebElement
    locators.update(chargeWidthField=('id', "width-voucher-form"))
    chargeLengthField: WebElement
    locators.update(chargeLengthField=('id', "length-voucher-form"))

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.collaboratorNameField.is_displayed())

    def waitPageVisible(self):
        time.sleep(2)
        self.waitElementDisplayed(self.locators.get('collaboratorNameField'))

    def waitPageNotVisible(self):

        self.waitElementNotDisplayed(self.locators.get('collaboratorNameField'))
        time.sleep(2)

    def setRadioValueForCompany(self, choice):
        self.setRadioValue(self.senderCompanyRadio, choice)

    def setRadioValueForPerson(self, choice):
        self.setRadioValue(self.senderPersonRadio, choice)


    def setVoucherSenderName(self, name):
        self.chooseDropDownType(self.senderNameField, name)

    def setVoucherSenderAddress(self, address):
        self.chooseDropDown(self.senderAdrressField, address)
        self.senderAdrressField.send_keys(Keys.ENTER)

    def setVoucherSenderPhoneNumber(self, phone):
        self.setTextField(self.senderPhoneField, phone)

    def setVoucherReceiverName(self, name):
        try:
            self.chooseDropDownType(self.recipientNameField, name)
        except:
            self.setTextField(self.recipientNameField, name)

    def setVoucherReceiverAddress(self, name):
        self.chooseDropDownType(self.recipientAddressField, name)

    def chooseVoucherReceiverAddressMap(self):
        ActionChains(self.driver).move_to_element_with_offset(self.recipientMap, 0, 0).perform()
        ActionChains(self.driver).context_click(self.recipientMap).perform()
        time.sleep(2)

    def setVoucherReceiverPhone(self, phone):
        self.setTextField(self.recipientPhoneField, phone)

    def setVoucherChargesType(self, choice):
        self.chooseDropDown(self.chargeTypeList, choice)

    def setVoucherPayAmount(self, amount):
        self.setTextField(self.chargeAmountField, amount)

    def iClickVoucherSubmitButton(self):
        self.submitVoucherButton.click()

    def setValuebyOrderCheckBox(self,state):
        self.setToogleValue(self.byOrderCheckbox,state)

    def setWithoutDeliveryCheckbox(self,state):
        self.setToogleValue(self.senderNoDeliveryCheckbox,state)

    def setDeliveryWithoutReceiptRadio(self,state):
        self.setToogleValue(self.deliveryVoucherRadio, state)

    def setNextDayDeliveryRadio(self,state):
        self.setToogleValue(self.pickupVoucherRadio, state)


    def setSameDayDeliveryRadio(self,state):
        self.setToogleValue(self.samedayVoucherRadio, state)

    def setCosignorNameField(self, name):
        self.chooseDropDownType(self.cosignorNameField, name)

