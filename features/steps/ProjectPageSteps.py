import time

from behave import *

from Utilities import configReader
from features.pageobjects.LoginPage import LoginPage
from features.pageobjects.ProjectDaysPage import ProjectDaysPage
from features.pageobjects.ProjectsPage import ProjectsPage
from features.steps import NavbarSteps


@when(u"I select project with name '{projectsName}'")
def iSelectProjectWithName(context, projectsName):
    context.projPage = ProjectsPage(context.driver)
    context.projPage.ichooseProjectWithName(projectsName)
    ProjectDaysPage(context.driver).waitPageVisible()

@when(u"I select the first project on the list")
def iSelectProjectWithName(context):
    context.projPage = ProjectsPage(context.driver)
    context.projPage.ichooseProjectWithOrder(1)
    ProjectDaysPage(context.driver).waitPageVisible()


