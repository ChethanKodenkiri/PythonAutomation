from behave import *
from selenium import webdriver
from pageObjects.loginPageObject import LoginPage
from configuration import baseUrl

@given('launch chrome browser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    


@when('open orange hrm homepage')
def open_orange_hrm_homepage(context):
    context.driver.get(baseUrl)


@then('verify that the logo present on page')
def verify_that_the_logo_present_on_page(context):
    try:
       status = LoginPage.isDisplayed(context.driver)
       assert status is True,"Logo is not present on the page."
    except Exception as e:
        print("An Error Occured ! ",e)


@then('close browser')
def close_browser(context):
    context.driver.close()

