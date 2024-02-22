from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by, value, timeout=10) -> WebElement:
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            raise NoSuchElementException

    def send_keys(self, by, value, keys):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(keys)

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def is_element_visible(self, by, value):
        element = self.find_element(by, value)
        return element.is_displayed()

    def is_element_enabled(self, by, value):
        element = self.find_element(by, value)
        return element.is_enabled()
