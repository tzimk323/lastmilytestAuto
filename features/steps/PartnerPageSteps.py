import time

from behave import *
from Utilities import configReader
from features.pageobjects.CollaboratorPartnerView import CollaboratorPartnerView
from features.pageobjects.CommonFunctions import CommonFunctions
from features.pageobjects.CustomersPage import CustomersPage
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.PartnersPage import PartnersPage
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.SettingPage import SettingsPage


@when("I click new partner button")
def iClickNewPartnerButton(context):
    PartnersPage(context.driver).iClickNewPartnersButton()
    PartnersPage(context.driver).waitNewPartnerModalVisible()


@when("I click from partner page history of shipments navigation button")
def iCLickFromParnetPageHistoryOfShipmentsNavigationButton(context):
    PartnersPage(context.driver).iClickShipmentsHistoryButton()
    PartnersPage(context.driver).waitShipmentsHistoryPageDisplayed()

@when("I click from partner page view partners navigation button")
def iCLickFromParnetPageViewPartnersNavigationButton(context):
    PartnersPage(context.driver).iClickViewPartnersButton()
    PartnersPage(context.driver).waitViewPartnersPageDisplayed()





@when("Verify from shipments history row '{row}' and column '{column}' holds the value: '{value}'")
def iCLickFromParnetPageHistoryOfShipmentsNavigationButton(context, row, column, value):
    actualCell = PartnersPage(context.driver).getFromShipmentHistoryNumberElementCellNumber(row, column)
    actualCell = actualCell.replace("\n", " ")
    # value=value+context.token
    assert actualCell == value


@when("I choose in view partner page the partner with name '{name}'")
def iCLickFromParnetPageHistoryOfShipmentsNavigationButton(context,name):
    PartnersPage(context.driver).choosePartnerWithName(name)
    CollaboratorPartnerView(context.driver).waitPageVisible()




@when("I fill new partners form with the following details")
def iFillNewPartnersFormWithTheFollowingDetails(context):
    PartnersPage(context.driver).iSetNewPartnerNameToBe(context.table[0]['Value'])
    if context.table[1]['Value'] == 'click':
        PartnersPage(context.driver).iSetNewPartnerAddressFromMapClick()
    else:
        PartnersPage(context.driver).iSetNewPartnerAddressTobe(context.table[1]['Value'])
    if context.table[2]['Value'] == 'random':
        email=CommonFunctions(context.driver).get_random_string(10) + "@gmail.com"
    else:
        email=context.table[2]['Value']
    context.email=email

    PartnersPage(context.driver).iSetNewPartnerEmailAddressTobe(email)
    PartnersPage(context.driver).iSetNewPartnerTaxIDToBe(context.table[3]['Value'])
    PartnersPage(context.driver).iSetNewPartnerTaxOfficeToBe(context.table[4]['Value'])


@when("I set in new partner modal new partner name to be '{name}'")
def iSetInNewpartnerModalNewPartnerNameToBe(context, name):
    PartnersPage(context.driver).iSetNewPartnerNameToBe(name)


@when("I set in new partner modal new partner address to be '{address}'")
def iSetInNewpartnerModalNewPartnerAddressToBe(context, address):
    PartnersPage(context.driver).iSetNewPartnerAddressTobe(address)


@when("I set in new partner modal new email address to be '{address}'")
def iSetInNewpartnerModalNewPartnerAddressToBe(context, address):
    PartnersPage(context.driver).iSetNewPartnerEmailAddressTobe(address)


@when("I set in new partner modal new partner tax id to be '{address}'")
def iSetInNewpartnerModalNewPartnerTaxIDToBe(context, address):
    PartnersPage(context.driver).iSetNewPartnerTaxIDToBe(address)


@when("I set in new partner modal new partner tax office to be '{address}'")
def iSetInNewpartnerModalNewPartnerTaxOfficeToBe(context, address):
    PartnersPage(context.driver).iSetNewPartnerTaxOfficeToBe(address)


@when("I click new partner modal submit button")
def iClickNewPartnerModalSubmitButton(context):
    PartnersPage(context.driver).iClickNewPartnerSubmitButton()
    PartnersPage(context.driver).waitNewPartnerModalNOTVisible()
