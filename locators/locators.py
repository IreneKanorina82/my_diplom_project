import os

from pages.base_page import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://belavia.by'

        super().__init__(web_driver, url)

    btn_headers_menu = WebElement(xpath='//div[@id="menu-dropdown"]//span[contains(text(),"Меню")]')
    btn_headers_bad_vision = WebElement(xpath='//div[@id="bad_vision"]//span[contains(text(),"Версия для слабовидящих")]')
    btn_headers_cloud = WebElement(xpath='//div[@id="ffp-account"]//span[contains(text(),"Личный кабинет")]')
    btn_headers_mail = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Почта")]')
    btn_setup_cookies = WebElement(id="accept")
    btn_footers_1_1 = WebElement(xpath='//div[@id="kontakty"]//span[contains(text(),"Контакты")]')
    btn_footers_1_2 = WebElement(xpath='//div[@id="time-table"]//span[contains(text(),"Расписание")]')
    btn_footers_1_3 = WebElement(xpath='//div[@id="table"]//span[contains(text(),"табло вылета/прилета")]')
    btn_footers_1_4 = WebElement(xpath='//div[@id="obrashheniya-grazhdan"]//span[contains(text(),"Обращения граждан")]')
    btn_footers_1_5 = WebElement(xpath='//div[@id="perevozka_gruzov"]//span[contains(text(),"Грузовые перевозки")]')
    btn_footers_2_1 = WebElement(xpath='//div[@id="agentam"]//span[contains(text(),"Агентам")]')
    btn_footers_2_2 = WebElement(xpath='//div[@id="onair"]//span[contains(text(),"Журнал OnAir")]')
    btn_footers_2_3 = WebElement(xpath='//div[@id="kontakty/obratnaya_svyaz"]//span[contains(text(),"Обратная связь")]')
    btn_footers_2_4 = WebElement(xpath='//div[@id="dlya-smi"]//span[contains(text(),"Для СМИ")]')
    btn_footers_2_5 = WebElement(xpath='//div[@id="https://www.mintrans.gov.by/ru/2024-god-kachestva"]//span[contains(text(),"2024 - Год качества")]')
    btn_language_english = WebElement(xpath='//div[@id="https://en.belavia.by/?newSite=1"]//span[contains(text(), "English")]')
    btn_language_belorussian = WebElement(xpath='//div[@id="https://by.belavia.by/?newSite=1"]//span[contains(text(), "Беларуская")]')
    btn_language_russian = WebElement(xpath='//div[@id="https://belavia.by/?newSite=1"]//span[contains(text(), "RU")]')
    btn_text_bar = WebElement(xpath='//a[@class="text-bar_visible-md"]//span[contains(text(),"Меню")]')


