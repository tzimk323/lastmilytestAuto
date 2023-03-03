import time

from behave import *
from Utilities import configReader
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.SettingPage import SettingsPage
from features.pageobjects.ZoneChargesPage import ZoneChargesPage


@when("I click to create new weight charge with details")
def iClickToCreateNewWeightChargeWithDetails(context):
    ZoneChargesPage(context.driver).iClickAddNewWeightCharge()
    ZoneChargesPage(context.driver).waitWeighChargeModalDisplayed()
    ZoneChargesPage(context.driver).chooseWeightChargesFromToDropDown(context.table[0]['Value'])
    ZoneChargesPage(context.driver).setWeightChargesAmount(context.table[1]['Value'])
    ZoneChargesPage(context.driver).chooseWeightChargesMeterDropDown(context.table[2]['Value'])
    ZoneChargesPage(context.driver).setWeightChargesNumber(context.table[3]['Value'])
    ZoneChargesPage(context.driver).iClickWeightModalSubmitButton()
    ZoneChargesPage(context.driver).waitWeighChargeModalNOTDisplayed()


@when("I click new weight charges modal button")
def iClickNewWeightChargesModalButton(context):
    ZoneChargesPage(context.driver).iClickAddNewWeightCharge()
    ZoneChargesPage(context.driver).waitWeighChargeModalDisplayed()


@when("I click zone charges charges page submit button")
def iClickZoneChargesSubmitButton(context):
    ZoneChargesPage(context.driver).iClickZoneChargesSubmitButton()


@when("I set weight charges amount field to be '{amount}'")
def iSetWeightChargesAmountFieldToBe(context,amount):
    ZoneChargesPage(context.driver).setWeightChargesAmount(amount)

@when("I set weight charges number field to be '{number}'")
def iSetWeightChargesNumberFieldToBe(context,number):
    ZoneChargesPage(context.driver).setWeightChargesNumber(number)


@when("I choose weight charges meter drop down to be '{choice}'")
def iSetWeightChargesAmountFieldToBe(context,choice):
    ZoneChargesPage(context.driver).chooseWeightChargesMeterDropDown(choice)


@when("I click weight charges modal the submit button")
def iSetWeightChargesAmountFieldToBe(context):
    ZoneChargesPage(context.driver).iClickWeightModalSubmitButton()
    ZoneChargesPage(context.driver).waitWeighChargeModalNOTDisplayed()

@when("I set name at zone charges modal to be '{name}'")
def iSetNameAtZoneChargesModalTobe(context,name):
    ZoneChargesPage(context.driver).iSetZoneChargesName(name)



@when("I choose weight charges number drop down to be '{choice}'")
def iSetWeightChargesAmountFieldToBe(context,choice):
    ZoneChargesPage(context.driver).chooseWeightChargesFromToDropDown(choice)

