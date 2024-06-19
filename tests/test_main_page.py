import pytest_check as check
from locators.locators import MainPage


def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    elements_headers = [
        page.btn_headers_domain,
    ]

    check.equal(page.btn_headers_domain.get_text(), 'Домены', 'Тест локатора не равен ожидаtмому результату')
    check.is_true(page.btn_headers_mail.is_visible())