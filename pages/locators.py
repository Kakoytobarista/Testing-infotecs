from selenium.webdriver.common.by import By


class MainPageLocators:
    HAMBURGER_UP_SIDE = (By.CSS_SELECTOR, "#main-navigation > li:nth-child(4) > a")
    PERSONAL_AREA = (By.CSS_SELECTOR, "body > div.main-nav > div:nth-child(6) > ul > li > a")
