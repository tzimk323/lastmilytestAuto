import time

from behave import *
from Utilities import configReader
from features.pageobjects.CustomersPage import CustomersPage
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.PartnersPage import PartnersPage
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.SettingPage import SettingsPage

@when("I fill new customer form with the following details")
def iFillNewCustomerFormWithTheFollowingDetails(context):
    CustomersPage(context.driver).setNewCustomerName(context.table[0]['Value'])
    CustomersPage(context.driver).setNewCustomerPhoneNumber(context.table[1]['Value'])
    if context.table[2]['Value'] == 'click':
        CustomersPage(context.driver).setNewCustomerAddressByMapClick()
    else:
        CustomersPage(context.driver).setNewCustomerAddress(context.table[2]['Value'])


@when("I click new customer button")
def iClickNewCustomerButton(context):
    CustomersPage(context.driver).iClickNewCustomerButton()
    CustomersPage(context.driver).waitNewCustomerPageDisplayed()

@when("I set in new customer modal new customer name to be '{name}'")
def iSetInNewCustomerModalNewCustomerNameToBe(context,name):
    CustomersPage(context.driver).setNewCustomerName(name)

@when("I set in new customer modal new customer phone number to be '{number}'")
def iSetInNewCustomerModalNewCustomerPhoneNumberToBe(context,number):
    CustomersPage(context.driver).setNewCustomerPhoneNumber(number)


@when("I set in new customer modal new customer address to be '{address}'")
def iSetInNewCustomerModalNewCustomerAddressToBe(context, address):
    CustomersPage(context.driver).setNewCustomerAddress(address)

@when("I click new customer modal submit button")
def iClickNewCustomerModalSubmitButton(context):
    CustomersPage(context.driver).clickNewCustomerModalSubmitButton()
    CustomersPage(context.driver).waitNewCustomerPageNotDisplayed()
