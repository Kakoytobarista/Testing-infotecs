from .base_page import BasePage


class MainPage(BasePage):
    def should_be_main_url(self):
        str_url = self.url
        print(str_url, "На этот адрес перешел")
        assert "https://infotecs.ru/" == str_url, "should be another url"

    def should_be_personal_area_url(self):
        str_url = self.url
        print(str_url)
        assert "https://infotecs.ru/cabinet/" == str_url, "url is not working"
