# -*- coding: utf-8 -*-
import time

from behave import *
from Utilities import configReader
from features.pageobjects.DashboardPage import DashboardPage
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.ProjectsPage import ProjectsPage
from features.pageobjects.RegisterInitPage import RegisterInitPage
from features.pageobjects.RegisterPage import RegisterPage



@given("I navigate at lastmily login page '{page}'")
def iVisitPage(context, page):
    context.log = LoginPage(context.driver)
    context.log.open(page)


@when("I fill login page username field with '{username}'")
def iFillLoginPageUsernameFieldWith(context, username):
    LoginPage(context.driver).fillLoginUserNameWith(username)

@when("I fill login page username field with previously registered email")
def iFillLoginPageUsernameFieldWith(context):
    LoginPage(context.driver).fillLoginUserNameWith(context.email)


@when("I fill login page password field with '{password}'")
def step_impl(context, password):
    LoginPage(context.driver).fillPassWordWith(password)


@when("I click the login button")
def iCLickTheLoginButton(context):
    LoginPage(context.driver).clickLoginButton()
    DashboardPage(context.driver).waitPageVisible()

@when("I click the login button to go to register initialization page")
def iCLickTheLoginButton(context):
    LoginPage(context.driver).clickLoginButton()
    RegisterInitPage(context.driver).waitPageVisible()

@when("I click register button")
def iClickRegisterButton(context):
    LoginPage(context.driver).clickLoginPageRegisterButton()
    RegisterPage(context.driver).waitPageVisible()


