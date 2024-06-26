import os

from page_test.pages.base_page import WebPage
from page_test.pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://belavia.by'

        super().__init__(web_driver, url)

    #headers
    btn_headers_menu = WebElement(xpath='//*[@class="text-bar visible-md" and contains(text(),"Меню")]')
    # btn_headers_bad_vision = WebElement(xpath='//div[@id="bad_vision"]//span[contains(text(),"Версия для слабовидящих")]')
    btn_headers_cloud = WebElement(xpath='//*[@id="lang-title" and contains(text(),"Личный кабинет")]')

    btn_lang_bar = WebElement(xpath='//a[@class="top-menu-item"]/span[@id="lang-title"]')

    btn_language_english = WebElement(xpath='//*[contains(text(),"English")]'),
    btn_language_belorussian = WebElement(xpath='//*[contains(text(),"Беларуская")]')
    btn_language_russian = WebElement(xpath='//*[contains(text(),"Русский")]')

    btn_set_cookies = WebElement(xpath='//*[contains(text(),"set_cookies")]')
    btn_footers_1_1 = WebElement(xpath='//*[contains(text(),"Кассы продаж")]')
    # btn_footers_1_2 = WebElement(xpath='//div[@id="time-table"]//span[contains(text(),"Расписание")]')
    btn_footers_1_3 = WebElement(xpath='//*[contains(text(),"Табло вылета/прилета")]')
    # btn_footers_1_4 = WebElement(xpath='//*[@href="obrashheniya-grazhdan"]//span[contains(text(),"Обращения граждан")]')
    # btn_footers_1_5 = WebElement(xpath='//*[@id="perevozka_gruzov"]/span[contains(text(),"Грузовые перевозки")]')
    btn_footers_2_1 = WebElement(xpath='//*[contains(text(),"Агентам")]')
    btn_footers_2_2 = WebElement(xpath='//*[contains(text(),"Журнал OnAir")]')
    btn_footers_2_3 = WebElement(xpath='//*[contains(text(),"Обратная связь")]')
    btn_footers_2_4 = WebElement(xpath='//*[contains(text(),"Для СМИ")]')
    btn_footers_2_5 = WebElement(xpath='//*[contains(text(),"2024 - Год качества")]')





