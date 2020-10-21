import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
import time

main_link = "https://infotecs.ru/"


class TestFromMainPage(object):
    def test_guest_can_go_to_main_page(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.should_be_main_url()

    def test_guest_can_click_to_hamburger(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.click_to_hamburger(browser)

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_can_go_to_personal_area(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.click_to_hamburger(browser)
        time.sleep(5)
        page.go_to_personal_area()
        time.sleep(5)
        page.should_be_personal_area_url()
