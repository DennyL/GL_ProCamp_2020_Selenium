from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BasePage:

    """ The base object that contains common to all the page objects in the app """

    def __init__(self, with_browser='chrome'):
        self.driver = webdriver.Remote(
            command_executor='http://192.168.1.103:4444/wd/hub',
            desired_capabilities=self.run_browser_from_stack(with_browser)
        )

    @staticmethod
    def run_browser_from_stack(browser_name):
        if browser_name.lower() == 'chrome':
            return DesiredCapabilities.CHROME
        elif browser_name.lower() == 'opera':
            return DesiredCapabilities.OPERA
        else:
            raise Exception('Browser name is not defined')

    def destroy_and_quit(self):
        self.driver.quit()
