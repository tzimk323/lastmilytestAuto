import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from features.pageobjects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory import PageFactory
import abc
import unittest

from features.pageobjects.CommonFunctions import CommonFunctions


class WizardPage(BasePage):
    #    Locators
    setCompanyButton: WebElement
    welcomeText: WebElement

    # depot section
    depotCustomInput: WebElement
    mapWizard: WebElement
    nextButtonWizard: WebElement
    nameDepotFormField: WebElement

    #   route section
    driverDepartureTime: WebElement
    sliderCSS: WebElement
    reloadToggle: WebElement
    slowDeliveryToggle: WebElement
    reloadSlider: WebElement

    #   delivery section
    loadField: WebElement
    portalAccessToggle: WebElement
    stopsForm: WebElement
    waitingDriverSlider: WebElement

    # vehicle section
    setCompanyButton: WebElement
    welcomeText: WebElement
    vehicleTypesOptions: WebElement
    numberOfVehicles: WebElement
    addAnotherVehicleBUtton: WebElement


    # # drivers settings
    driverOverimeToggle: WebElement
    driverMaxWorkingHours: WebElement
    # welcomeText: WebElement

    # drivers section
    nameOfDriverFormField: WebElement
    telephoneOfDriverField: WebElement
    departureTimeOfDriver: WebElement
    driversHoursField: WebElement
    addDriverButton: WebElement
    chooseTypeOfVehicleField: WebElement
    wizardFinishButton: WebElement


    driver: WebDriver

    locators = {
        'setCompanyButton': ('id', "setCompanyButton"),
        'welcomeText': ('id', 'welcomeText'),

        # depot section
        'depotCustomInput': ('id', "depot-custom-input"),
        'mapWizard': ('id', 'map'),
        'nextButtonWizard': ('id', "nextButton"),
        'nameDepotFormField': ('id', "name-depot-form"),

        #   route section
        'driverDepartureTime': ('id', "departure-time-settings-form"),
        'sliderCSS': ('css_selector', "div[role='slider']"),
        'reloadToggle': ('id', "reload_system_switch"),
        'slowDeliveryToggle': ('id', 'allow_late_stops'),
        'reloadSlider': ('id', "sliderReload"),

        #   delivery section
        'loadField': ('id', "default-load-settings-form"),
        'portalAccessToggle': ('id', "portal_access_toggle"),
        'stopsForm': ('id', "stops-form"),
        'waitingDriverSlider': ('id', 'waitingDriverSlider'),

        # vehicle section
        'vehicleTypesOptions': ('id', "vehicle-types"),
        'maxLitersToloadField': ('id', "vehicle-cargo-capacity-vehicle-form"),
        'numberOfVehicles': ('id', "vehicle-count-vehicle-form"),
        'addAnotherVehicleBUtton': ('id', 'add_another_vehicle_button'),

        # drivers settings
        'driverOverimeToggle': ('id', "driver_overtime"),
        'driverMaxWorkingHours': ('id', "drivers_working_hours"),

        # drivers settings
        'nameOfDriverFormField': ('id', "name-driver-form"),
        'telephoneOfDriverField': ('id', "telephone-driver-form"),
        'departureTimeOfDriver': ('id', "departure-time-driver-form"),
        'driversHoursField': ('id', 'working-hours-driver-form'),
        'addDriverButton': ('id', "add-driver-button"),
        'chooseTypeOfVehicleField': ('id', "vehicle_type_listbox"),
        'wizardFinishButton': ('id', "wizard-finish-button"),
    }

    def __init__(self, driver):
        super().__init__(driver)

    def isPageDisplayed(self):
        return self.assertTrue(self.welcomeText.is_displayed())

    def waitPageVisible(self):
        self.waitElementDisplayed(self.locators['welcomeText'])

    def clickSetCompanyButton(self):
        self.setCompanyButton.click()

    def waitWizardPage1Visible(self):
        self.waitElementDisplayed(self.locators['depotCustomInput'])
        self.waitPageToLoad()
        self.waitPageToLoad() # time.sleep(2)

    def waitWizardPageRouteSectionVisible(self):
        self.waitElementDisplayed(self.locators['driverDepartureTime'])
        self.waitPageToLoad()

    def waitWizardPageDeliverySectionVisible(self):
        self.waitElementDisplayed(self.locators['loadField'])
        self.waitPageToLoad()

    def waitWizardPageVehicleSectionVisible(self):

        self.waitElementDisplayed(self.locators['vehicleTypesOptions'])
        self.waitPageToLoad()

    def waitWizardPageDriverSectionVisible(self):
        self.waitElementDisplayed(self.locators['driverMaxWorkingHours'])
        self.waitPageToLoad()

    def waitWizardPageDriverSettingsVisible(self):
        self.waitElementDisplayed(self.locators['nameOfDriverFormField'])
        self.waitPageToLoad()

    def clickWizardNextButton(self):
        self.nextButtonWizard.click()

    def rightClickOnMapToChooseAddressWithCoord(self, x, y):
        ActionChains(self.driver).move_to_element_with_offset(self.mapWizard, x, y).perform()
        ActionChains(self.driver).context_click(self.mapWizard).perform()
        self.waitPageToLoad() # time.sleep(2)
        self.waitPageToLoad()

    def getTextFromDepotField(self):
        return self.depotCustomInput.text

    def setNameOfDepot(self, name):
        self.setTextField(self.nameDepotFormField, name)

    def slowDeliveryTooggleState(self, state):
        self.setToogleValue(self.slowDeliveryToggle, state)

    def reloadTooggleState(self, state):
        self.setToogleValue(self.reloadToggle, state)

    def setReloadTimeSlider(self, value):
        self.setSliderValue(self.reloadSlider, value, 5)

    def setUsualLoad(self, value):
        self.setTextField(self.loadField, value)

    def setLastmilyAccessToggle(self, state):
        self.setToogleValue(self.portalAccessToggle, state)

    def setVehicleMaxLoad(self, load):
        self.setTextField(self.maxLitersToloadField, load)
    def setVehicleNumber(self, num):
        self.setTextField(self.numberOfVehicles, num)

    def clickAddVehicleButton(self):
        self.addAnotherVehicleBUtton.click()
        time.sleep(1)
        self.waitPageToLoad()

    def setDriverOvertimeToggle(self,state):
        self.setToogleValue(self.driverOverimeToggle, state)

    def setDriverName(self, name):
        self.setTextField(self.nameOfDriverFormField, name)

    def setDriverphone(self, number):
        if number.lower() == 'random':
            number= CommonFunctions(self.driver).get_random_number(10)
        self.setTextField(self.telephoneOfDriverField, number)

    def setDriverhours(self, hours):
        self.setTextField(self.driversHoursField, hours)

    def chooseDriverVehicleType(self, typeof):
        self.chooseDropDownText(self.chooseTypeOfVehicleField, typeof)
        self.waitPageToLoad()
        # self.skee.sleep(1)
    def iclickWizardFinishButton(self):
        self.wizardFinishButton.click()
        self.waitPageToLoad()
        # self.skee.sleep(1)


    def clickAddDriverButton(self):
        self.addDriverButton.click()
        self.waitPageToLoad() # time.sleep(2)

    def chooseVehicleType(self, type):
        vehicleTypes = {
            "bicycle": 0,
            "motor": 1,
            "van": 2,
            "small-truck": 3,
            "mid-truck": 4,
            "big-truck": 5,
        }
        if type.lower() in vehicleTypes:
            index = vehicleTypes.get(type.lower())
        else:
            raise Exception("Vehicle type does not exist")
        self.vehicleTypesOptions.find_element(By.CSS_SELECTOR, f"div[index='{index}']").click()
