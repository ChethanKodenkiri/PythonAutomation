from configuration import baseUrl
class Helper:
    def __init__(self,driver):
        self.driver = driver

    def loginToSite(self):
        self.driver.get(baseUrl)