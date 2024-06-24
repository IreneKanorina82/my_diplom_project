import allure
import pytest_check as check
from pages.base_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедера')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    page.btn_set_cookies.click()

    elements_headers = [
        (page.btn_headers_menu, 'Меню'),
        (page.btn_headers_bad_vivion, 'Версия для слабовидящих')
        (page.btn_headers_RU, 'Русский'),
        (page.btn_headers_cloud, 'Личный кабинет'),
        (page.btn_headers_mail, 'Обычная версия')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Проверка "{elements_text}" на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста"{elements_text}"'):
            check.equal(elements.get_text(), elements_text)



