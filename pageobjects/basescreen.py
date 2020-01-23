from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseScreen(object):

    def __init__(self, driver):
        self.driver = driver
        self.title = driver.instance.title

    def select_element(self, locator):
        """Select an element by waiting for it to become visible"""
        wait = WebDriverWait(self.driver.instance, 16)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    def wait_until_clickable(self, locator):
        wait = WebDriverWait(self.driver.instance, 16)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

