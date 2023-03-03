import time

from behave import *
from Utilities import configReader
from features.pageobjects.CollaboratorPartnerView import CollaboratorPartnerView
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.Navbar import Navbar
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.SettingPage import SettingsPage
from features.pageobjects.ZoneChargesPage import ZoneChargesPage


@when("I choose from collaborator partner view page the stop point nav button")
def iChooseFromCollaboratorViewPageStopPointNavButton(context):
    CollaboratorPartnerView(context.driver).iChooseFromCollaboratorViewNavbarOptionWithOrder(6)
    CollaboratorPartnerView(context.driver).waitCollaboratorViewStopPointPageVisible()

@when("I choose from collaborator partner view page the stop point nav button partners")
def iChooseFromCollaboratorViewPageStopPointNavButtonPartners(context):
    CollaboratorPartnerView(context.driver).iChooseFromCollaboratorViewNavbarOptionWithOrder(7)
    time.sleep(2)

@when("I choose from collaborator view page the invoice filter button")
def iCghooseFromCollaboratorViewPageTheInvoiceFilterButton(context):
    CollaboratorPartnerView(context.driver).iChooseCollaboratorFilterInvoiceButton()
    time.sleep(3)

@when("I choose from partner view page the invoice filter button")
def iCghooseFromCollaboratorViewPageTheInvoiceFilterButton(context):
    CollaboratorPartnerView(context.driver).iChoosePartnerFilterInvoiceButton()
    time.sleep(3)
@when("I choose from collaborator partner view page the manual invoice button")
def iCghooseFromCollaboratorViewPageTheManualInvoiceButton(context):
    CollaboratorPartnerView(context.driver).iChooseColaboratorPartnerManualInvoiceButton()
    time.sleep(3)

@when("I choose to invoice the stop point with creation date '{creationdate}'")
def iCghooseToInvoiceStopPointWithCreationDate(context,creationdate):
    CollaboratorPartnerView(context.driver).iCheckForInvoiceTheStopPointWithCreationDate(creationdate)
    time.sleep(1)

@when("I choose to invoice the stop point with address '{address}'")
def iCghooseToInvoiceStopPointWithAddress(context,address):
    CollaboratorPartnerView(context.driver).iCheckForInvoiceTheStopPointWithAddress(address)
    time.sleep(1)

@when("I click the invoice button")
def iCghooseFromCollaboratorViewPageTheManualInvoiceButton(context):
    CollaboratorPartnerView(context.driver).iclickInvoiceButton()
    time.sleep(1)


@then("Verify from invoice at row '{row}' and column '{col}' holds the value: '{text}'")
def verifyFromInVoiceAtRowAndCOlumnHoldsTheValue(context, row,col,text):
    actualCell=CollaboratorPartnerView(context.driver).getFromInvoiceElementsCellNumber(row,col)
    actualCell = actualCell.replace("\n", " ")

    # value=value+context.token
    assert actualCell == text


@when("I click from the invoice of number '{num}' the action approved button")
def iCghooseFromCollaboratorViewPageTheManualInvoiceButton(context,num):
    CollaboratorPartnerView(context.driver).iclickFromInvoiceNumberTheActionButton(num)
    time.sleep(2)







