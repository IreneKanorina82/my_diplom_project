
import allure
import pytest_check as check
# from page_test.pages.base_page import MainPage
from page_test.pages.locators import MainPage
import time


@allure.story('Проверка главной страницы')
@allure.feature('Проверка меню "Настройки языка"')
def test_language_buttons(web_browser):
    """Тест проверяет кнопки языка в настройках"""

    page = MainPage(web_browser)

    page.scroll_down()
    time.sleep(1)

    page.language_button.click()
    time.sleep(1)

    language_buttons = [
        (page.btn_russian, "Русский"),
        (page.btn_english, "English"),
        (page.btn_belorussian, "Беларуская")
        ]

    for language_button in language_buttons:
        language_button.scroll_to_element()

        with allure.step(f'Проверка элемента на наличие'):
            check.is_true(language_button.is_presented(), f'language_button is not presented')

        with allure.step(f'Проверка текста элемента на отображение'):
            check.is_true(language_button.is_visible(), f'language_button text is not displayed')

        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(language_button.is_clickable(), f'language_button is not clickable')

        with allure.step(f'Проверка, что элемент выбран'):
            language_button.click()
            time.sleep(2)
            check.is_true(language_button.is_selected(), f'language_button is not selected')

@allure.story('Проверка главной страницы')
@allure.feature('Проверка меню "Настройки языка"')
def test_settings_checkboxes(web_browser):
    """Тест проверяет параметры выбора языка в настройках"""

    page = MainPage(web_browser)

    page.scroll_down()
    time.sleep(1)

    page.btn_language.click()
    time.sleep(1)

    checkboxes = [
        (page.checkbox_russian, page.checkbox_russian_label, "Русский"),
        (page.checkbox_english, page.checkbox_english_label, "Английский")
    ]

    for checkbox, checkbox_label, required_checkbox_text in checkboxes:
        checkbox.scroll_to_element()

        with allure.step(f'Проверка элемента "{required_checkbox_text}" на наличие'):
            check.is_true(checkbox_label.is_presented(), f'Checkbox {required_checkbox_text} is not presented')

        with allure.step(f'Проверка текста элемента "{required_checkbox_text}" на отображение'):
            check.is_true(checkbox_label.is_visible(), f'Checkbox text {required_checkbox_text} is not displayed')

        with allure.step(f'Проверка элемента "{required_checkbox_text}" на кликабельность'):
            check.is_true(checkbox_label.is_clickable(), f'Checkbox {required_checkbox_text} is not clickable')

        with allure.step(f'Проверка, что элемент "{required_checkbox_text}" выбран'):
            if checkbox.is_selected() is False:
                checkbox_label.click()
                time.sleep(1)
            check.is_true(checkbox.is_selected(), f'Checkbox {required_checkbox_text} is not selected')

    for checkbox, checkbox_label, required_checkbox_text in checkboxes:
        checkbox.scroll_to_element()
        if checkbox.is_selected():
            checkbox_label.click()

    with allure.step(f'Проверка появления предупреждающего текста'):
        check.is_true(page.checkbox_warning.is_visible(), f'Checkbox warning is not displayed')
        warning_text = page.checkbox_warning.get_text()
        check.equal(warning_text, 'Должен быть выбран хотя бы один язык', f'Текст предупреждающего уведомления не равен ожидаемому')