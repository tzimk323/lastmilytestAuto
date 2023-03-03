import time

from behave import *
from Utilities import configReader
import random

from features.pageobjects.CommonFunctions import CommonFunctions
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.RegisterPage import RegisterPage


@when("I fill register form with following details and register mail")
def verifyThatTheProjectDayWithNameHasTheFollowingDetails(context):
    context.register = RegisterPage(context.driver)
    context.register.fillRegisterNameField(context.table[0]['Value'])
    if context.table[1]['Value'].lower() == 'random':
        company= CommonFunctions(context.driver).get_random_string(12)
        context.company_name = company
    elif context.table[1]['Value'].lower() == 'random2':
        company = CommonFunctions(context.driver).get_random_string(12)
        context.company_name2 = company
    else:
        company=context.table[1]['Value']
        context.company_name = company

    context.register.fillRegisterCompanyNameField(company)
    if context.table[2]['Value'].lower() == 'random':
        email = CommonFunctions(context.driver).get_random_string(10) + "@gmail.com"
    else:
        email = context.table[2]['Value']

    context.register.fillRegisterEmailField(email)
    context.email=email
    context.register.fillRegisterPasswordField(context.table[3]['Value'])
    context.register.fillRegisterPhoneField(context.table[4]['Value'])
    CommonFunctions(context.driver).waitPageToLoad()
    time.sleep(2)

    # for row in context.table:
    #     row['Value']


@then("I click in register page go button")
def iCLickInRegisterPageGoButton(context):
     context.register.clickRegisterGoButton()
     context.register.waitMailConfirmationDisplayed()


@then("I click in register page the login link")
def iClickInRegisterPageTheLoginLink(context):
     context.register.clickLoginLink()
     context.log= LoginPage(context.driver).waitPageVisible()

