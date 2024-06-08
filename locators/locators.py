import os

from my_diplom.pages.base_page import WebPage
from my_diplom.pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://belavia.by/'

        super().__init__(web_driver, url)

    btn_headers_menu = WebElement(xpath='//div[@id="menu-dropdown"]//span[contains(text(),"Меню")]')
    btn_headers_bad_vision = WebElement(xpath='//div[@id="bad_vision"]//span[contains(text(),"Версия для слабовидящих")]')
    btn_headers_cloud = WebElement(xpath='//div[@id="ffp-account"]//span[contains(text(),"Личный кабинет")]')
    btn_headers_mail = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Почта")]')

