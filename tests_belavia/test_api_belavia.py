import allure
import pytest_check as check
import time
from pages.base_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности инпута')
def test_input_main(web_browser):
    """Этот тест проверяет работоспособность инпута"""

    page = MainPage(web_browser)

    page.btn_set_сookies.click()

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.input_id_transfer.is_visible(page, MainPage))

    with allure.step('Проверка на отображение'):
        check.is_true(page.input_id_transfer.is_clickable(page, MainPage))

    with allure.step('Проверка плейсхолдера'):
        check.equal(page.input_id_transfer.get_attribute('placeholder'), 'Откуда')

    with allure.step('Проверка на ввод текст и проверка результата'):
        text_by_zone = page.text_by_zone.get_text()
        text_cockicock = 'cockicock'

        page.input_id_transfer.send_keys(text_cockicock)
        page.btn_text_bar.click(1)

        time.sleep(10)
        print(page.group_valid_domain.get_text())
        check.not_equal(page.group_valid_domain.get_text().find(f'{text_cockicock+text_by_zone}'), -1)
