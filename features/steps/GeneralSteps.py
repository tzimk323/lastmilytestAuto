import time

from behave import *

from Utilities import configReader
from features.pageobjects.CommonFunctions import CommonFunctions
from features.pageobjects.DatabaseActions import DatabaseActions
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.MailServer import MailServer
from features.pageobjects.ProjectViewPage import ProjectViewPage
from features.pageobjects.RegisterPage import RegisterPage


@when("I start performance tracing with dev tools")
def iStartPerformanceDevtools(context):
    context.CF = CommonFunctions(context.driver)
    context.CF.startTracing(context.tab)


@when("I save my data to the datafile")
def iSaveMydataToTheDatafile(context):
    context.CF = CommonFunctions(context.driver)
    dataField1=context.table[0]['Field']
    dataField2=context.table[1]['Field']
    data=[]
    data.append({dataField1:context._stack[0][dataField1]})
    data.append({dataField2:context._stack[0][dataField2]})
    context.CF.saveDataToDatafile(data)


@when("I stop performance tracing with dev tools and i save the file to '{fileName}'")
def iStopPerformanceDevTools(context, fileName):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.stopTracing(context.tab, fileName)

@when("SCENARIO SECTION: '{name}'")
def scenarioSection(context, name):
    print("\n Scenario section : ")
    print(name)

@when("I stop performance tracing with dev tools and i save the file to '{fileName}' where i edit log file for duration of js events")
def iStopPerformanceDevToolsAndISaveFileWhereIEditLogFIleForDuraionOfJsEvents(context, fileName):
    context.ProjectView = ProjectViewPage(context.driver)
    context.ProjectView.stopTracingEditLogfile(context.tab, fileName)


@when("I send command via CDP to emulate a cpu with throttling rate of '{rate}'")
def iStartPerformanceDevtools(context, rate: int):
    context.CF = CommonFunctions(context.driver)
    context.CF.emaluteCPUthrottleRate(context.tab,rate)


@when("I continue my navigation from the link of the sender email to register")
def iContinueMyNavigationFromTheLinkOfTheSenderEmailToRegister(context):
   token= DatabaseActions().getLatestInviteLink()
   link="http://localhost/register/collaborator/"+token
   context.token=token
   context.driver.get(link)
   RegisterPage(context.driver).waitPageVisible()



@then("I refresh the page")
def iRefreshThePage(context):
    context.CF = CommonFunctions(context.driver)
    context.CF.refreshPage()
    context.CF.waitPageToLoad() # time.sleep(3)