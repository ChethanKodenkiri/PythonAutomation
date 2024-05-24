from behave import given, when, then
from Helper.helper import Helper
from selenium import webdriver


@given('User starts sole onboarding journey by filling details')
def step_given_user_starts_sole_onboarding_journey(context):
    context.driver=webdriver.Chrome()
    Helper.loginToSite(context.driver)


@when('User fills personal details and proceeds with mobile and email verification')
def step_when_user_fills_personal_details(context):
    # Code to fill personal details
    # Code to proceed with mobile verification
    # Code to proceed with email verification
    pass

@then('User sets password and validates the same with Cognito OTP validation')
def step_then_user_sets_password(context):
    # Code to set the password
    # Code to validate password with Cognito OTP
    pass

@then('User completes Additional and Nominated details')
def step_then_user_completes_additional_details(context):
    # Code to complete additional details
    # Code to complete nominated details
    pass

@then('User reviews the details entered')
def step_then_user_reviews_details(context):
    # Code to review the details entered
    pass

@then('User completes the sole onboarding journey')
def step_then_user_completes_journey(context):
    # Code to complete the sole onboarding journey
    pass

@then('User validates the details against Mambu and CRM APIs')
def step_then_user_validates_against_apis(context):
    # Code to validate the details against Mambu API
    # Code to validate the details against CRM API
    pass
