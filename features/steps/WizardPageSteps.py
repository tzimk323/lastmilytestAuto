import time
from unittest import TestCase

from behave import *
from Utilities import configReader
from features.pageobjects.CommonFunctions import CommonFunctions
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.WizardPage import WizardPage





@when("I fill wizard pages with my default values")
def iFillWizardPagesWithmydefaultvalues(context):
    iRightClickOnWizardMapToChooseDepotAddress(context, 0, 0)
    iSetWizardNameOfDepotToBe(context, "the best depot")
    iClickNextWizardButtonToGotoRouteSection(context)
    iSetToBeAllowedTheSlowDeliverTo(context, True)
    iSetTheToggleToBeStateAtDriversReturnForLoad(context, True)
    iSetTheSliderOfTimeOfReloadingToBe(context, 40)
    iClickNextWizardButtonToGotoDeliverySection(context)
    iSetTheUsualLoadToBe(context, 100)
    iSetTheLastmilyAccessToggleToBe(context, True)
    iClickNextWizardButtonToGotoVehicleSection(context)
    iChooseFromWizardPageTypeOfVehicle(context, "motor")
    iSetNumberOfSelectedVehiclesToBe(context, 3)
    iSetMaximumLoadOfSelectedVehiclesToBe(context, 6000)
    iClickToAddVehicleButton(context)
    iClickNextWizardButtonToGotoDriversSection(context)
    iSetTheMaximumOverTimeToggleToBe(context, True)
    iClickNextWizardButtonToGotoDriversSettingsSection(context)
    iChooseNameOfDriverToBe(context,"Giwrgos")
    iChoosePhoneNumberOfDriverToBe(context, "random")
    iSetDriverMaximumWorkingHoursToBe(context, 8)
    iChooseDriversVehicleOwnershipFromDropDownToBe(context, "Μηχανάκι")
    iClickInWizardPAgeToAddDriverButton(context)
    iChooseNameOfDriverToBe(context, 'panos')
    iChoosePhoneNumberOfDriverToBe(context, "random")
    iSetDriverMaximumWorkingHoursToBe(context, "9")
    iChooseDriversVehicleOwnershipFromDropDownToBe(context, 'Μεγάλο Βάν')
    iClickInWizardPAgeToAddDriverButton(context)
    iCLickWizardFinishButton(context)


@when("Verify that the wizard page is visible")
def VerifyThatTheWizardPageVisible(context):
    context.wizard = WizardPage(context.driver).isPageDisplayed()
    ProjectsPage(context.driver).waitPageVisible()


@when("I click wizard page set company button")
def VerifyThatTheWizardPageVisible(context):
    context.wizard = WizardPage(context.driver).clickSetCompanyButton()
    WizardPage(context.driver).waitWizardPage1Visible()


@when("I right click on wizard map to choose depot address with coordinates '{x}' and '{y}'")
def iRightClickOnWizardMapToChooseDepotAddress(context, x, y):
    WizardPage(context.driver).rightClickOnMapToChooseAddressWithCoord(x, y)


@when('Verify that depot address is the following "{address}"')
def verifyThatDepotAddressIsTheFollowing(context, address):
    actualText = WizardPage(context.driver).getTextFromDepotField()
    TestCase().assertEqual(address, actualText)


@when('I set wizard name of depot to be "{depotname}"')
def iSetWizardNameOfDepotToBe(context, depotname):
    WizardPage(context.driver).setNameOfDepot(depotname)


@when("I click next wizard button to go to route section")
def iClickNextWizardButtonToGotoRouteSection(context):
    WizardPage(context.driver).clickWizardNextButton()
    WizardPage(context.driver).waitWizardPageRouteSectionVisible()


@when("I click next wizard button to go to delivery section")
def iClickNextWizardButtonToGotoDeliverySection(context):
    WizardPage(context.driver).clickWizardNextButton()
    WizardPage(context.driver).waitWizardPageDeliverySectionVisible()


@when("I click next wizard button to go to drivers section")
def iClickNextWizardButtonToGotoDriversSection(context):
    WizardPage(context.driver).clickWizardNextButton()
    WizardPage(context.driver).waitWizardPageDriverSectionVisible()


@when("I click next wizard button to go to drivers settings section")
def iClickNextWizardButtonToGotoDriversSettingsSection(context):
    WizardPage(context.driver).clickWizardNextButton()
    WizardPage(context.driver).waitWizardPageDriverSettingsVisible()


@when("I click next wizard button to go to vehicle section")
def iClickNextWizardButtonToGotoVehicleSection(context):
    WizardPage(context.driver).clickWizardNextButton()
    WizardPage(context.driver).waitWizardPageVehicleSectionVisible()


@when("I click next wizard button")
def iClickNextWizardButton(context):
    WizardPage(context.driver).clickWizardNextButton()


@when('I set time of drivers arrival to be "{time}"')
def iSetTimeOfDriversArrivalToBe(context, time):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I set time of drivers arrival to be "8:10"')


@when("I set to be allowed the slow deliver to '{state}'")
def iSetToBeAllowedTheSlowDeliverTo(context, state):
    WizardPage(context.driver).slowDeliveryTooggleState(state)


@when('I set the toggle to be "{state}" at drivers return for load')
def iSetTheToggleToBeStateAtDriversReturnForLoad(context, state):
    WizardPage(context.driver).reloadTooggleState(state)


@when('I set the slider of time of reloading to be "{value}"')
def iSetTheSliderOfTimeOfReloadingToBe(context, value):
    WizardPage(context.driver).setReloadTimeSlider(value)


@when('I set the slider of drivers waiting time to be "{value}"')
def iSetTheSliderOfDriversWaitingTimeToBe(context, value):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I set the slider of drivers waiting time to be ""')


@when('I set the usual load to be "{load}"')
def iSetTheUsualLoadToBe(context, load):
    WizardPage(context.driver).setUsualLoad(load)


@when('I set the lastmily access toggle to be "{state}"')
def iSetTheLastmilyAccessToggleToBe(context, state):
    WizardPage(context.driver).setLastmilyAccessToggle(state)


@when('I choose from wizard page type of vehicle "{type}"')
def iChooseFromWizardPageTypeOfVehicle(context, type):
    WizardPage(context.driver).chooseVehicleType(type)


@when('I set number of selected vehicles to be "{number}"')
def iSetNumberOfSelectedVehiclesToBe(context, number):
    WizardPage(context.driver).setVehicleNumber(number)


@when('I set maximum load of selected vehicles to be "{maxLoad}"')
def iSetMaximumLoadOfSelectedVehiclesToBe(context, maxLoad):
    WizardPage(context.driver).setVehicleMaxLoad(maxLoad)


@when("I click to add vehicle button")
def iClickToAddVehicleButton(context):
    WizardPage(context.driver).clickAddVehicleButton()


@when('I choose maximum working hours slider to be "{maxhours}"')
def iChooseMaximumWorkingHoursSliderToBe(context, maxhours):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I choose maximum working hours slider to be ""')


@when('I set the maximum driver overtime toggle to be "{time}"')
def iSetTheMaximumOverTimeToggleToBe(context, time):
    WizardPage(context.driver).setDriverOvertimeToggle(time)


@when('I choose name of driver to be "{name}"')
def iChooseNameOfDriverToBe(context, name):
    WizardPage(context.driver).setDriverName(name)


@when('I choose phone number of driver to be "{number}"')
def iChoosePhoneNumberOfDriverToBe(context, number):
    WizardPage(context.driver).setDriverphone(number)


# @when('I set driver departure time to be "{time}"')
# def iSetDriverDepartureTimeToBe(context, time):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: When I set driver departure time to be ""')


@when('I set driver maximum working hours to be "{number}"')
def iSetDriverMaximumWorkingHoursToBe(context, number):
    WizardPage(context.driver).setDriverhours(number)



@when('I choose drivers vehicle ownership from drop down to be "{vehicle}"')
def iChooseDriversVehicleOwnershipFromDropDownToBe(context, vehicle):
    WizardPage(context.driver).chooseDriverVehicleType(vehicle)


@when("I click in wizard page the add driver button")
def iClickInWizardPAgeToAddDriverButton(context):
    WizardPage(context.driver).clickAddDriverButton()


@when("I click wizard finish button")
def iCLickWizardFinishButton(context):
    WizardPage(context.driver).iclickWizardFinishButton()
    DashboardPage(context.driver).waitPageVisible()
    CommonFunctions(context.driver).waitPageToLoad()
    time.sleep(2)