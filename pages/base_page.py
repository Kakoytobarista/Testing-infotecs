from .locators import MainPageLocators
from selenium import webdriver


class BasePage(object):
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        print("\nopen page")

    def click_to_hamburger(self, driver):
        self.browser.find_element(*MainPageLocators.HAMBURGER_UP_SIDE).click()
        driver.set_window_size(600, 600)

    def go_to_personal_area(self):
        self.browser.find_element(*MainPageLocators.PERSONAL_AREA).click()
