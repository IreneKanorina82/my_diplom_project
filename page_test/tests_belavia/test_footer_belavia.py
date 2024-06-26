import allure
import pytest_check as check
from page_test.pages.locators import MainPage
import time


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки футера')
def test_footers(web_browser):
    """Этот тест проверяет футер главной страницы"""

    page = MainPage(web_browser)

    """page.btn_set_сookie.click()"""

    elements_footers = [
        (page.btn_footers_1_1, 'Кассы продаж'),
        # (page.btn_footers_1_2, 'Расписание'),
        (page.btn_footers_1_3, 'Табло вылета/прилета'),
        # (page.btn_footers_1_4, 'Обращения граждан'),
        # (page.btn_footers_1_5, 'Грузовые перевозки'),
        (page.btn_footers_2_1, 'Агентам'),
        (page.btn_footers_2_2, 'Журнал OnAir'),
        (page.btn_footers_2_3, 'Обратная связь'),
        (page.btn_footers_2_4, 'Для СМИ'),
        (page.btn_footers_2_5, '2024 - Год качества')
        ]

    page.scroll_down()
    time.sleep(1)

    for elements, elements_text in elements_footers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Проверка "{elements_text}" на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста"{elements_text}"'):
            check.equal(elements.get_text(), elements_text)
