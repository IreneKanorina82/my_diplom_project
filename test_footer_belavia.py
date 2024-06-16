import allure
import pytest_check as check
from pages.base_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки футера')
def test_footers(web_browser):
    """Этот тест проверяет футер главной страницы"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_footers = [
        (page.btn_footers_kontakty, 'Контакты'),
        (page.btn_footers_table, 'Табло вылета/прилета'),
        (page.btn_headers_agentam, 'Агентам'),
        (page.btn_headers_onair, 'Журнал OnAir')
        ]

    for elements, elements_text in elements_footers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Проверка "{elements_text}" на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста"{elements_text}"'):
            check.equal(elements.get_text(), elements_text)

