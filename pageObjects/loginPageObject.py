from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def isDisplayed(self):
        logo_Locator = (By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[1]/img')
        return self.driver.find_element(*logo_Locator).is_displayed()