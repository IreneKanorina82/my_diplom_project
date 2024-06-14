# noinspection PyUnresolvedReferences
import allure
import pytest_check as check
import time
import unittest
from pages.base_page import MainPage
from pages.base_page import WebPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from termcolor import colored



class WebElement(object):

    _locator = ('MainPage', WebPage 'https://belavia.by/')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = False  # TODO: how we can wait after click?

    def __init__(self, timeout=10, wait_after_click=False, **kwargs):
        self._timeout = timeout
        self._wait_after_click = wait_after_click

        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self, timeout=10):
        """ Find element on the page. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_element_located(self._locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element

    def is_clickable(self):
        """ Check is element ready for click or not. """

        element = self.wait_to_be_clickable(timeout=1)
        return element is not None

    def is_presented(self):
        """ Check that element is presented on the page. """

        element = self.find(timeout=1)
        return element is not None

    def is_visible(self):
        """ Check is the element visible or not. """

        element = self.find(timeout=1)

        if element:
            return element.is_displayed()

        return False


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедера')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.btn_headers_menu, 'Меню'),
        (page.btn_headers_RU, 'Русский'),
        (page.btn_headers_ffpAccount, 'Личный кабинет'),
        (page.btn_headers_bad_vision, 'Обычная версия')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Проверка "{elements_text}" на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста"{elements_text}"'):
            check.equal(elements.get_text(), elements_text)

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки наличия блоков')
def test_headers(web_browser):
    """Этот тест проверяет блоки главной страницы на его присутствие"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.block_main, 'Первый блок или главный')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки текста')
def test_headers(web_browser):
    """Этот тест проверяет текст на наличие и его корректность"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.txt_main_h1, 'Belavia')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Сверка текста "{elements_text}"'):
            check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности инпута')
def test_input_main(web_browser):
    """Этот тест проверяет работоспособность инпута"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.input_main_wrapper.is_visible())

    with allure.step('Проверка на отображение'):
        check.is_true(page.input_main_wrapper.is_clickable())

    with allure.step('Проверка плейсхолдера'):
        check.equal(page.input_main_wrapper.get_attribute('placeholder'), 'Откуда')

    with allure.step('Проверка на ввод текст и проверка результата'):
        text_by_zone = page.text_by_zone.get_text()
        text_cockicock = 'cockicock'

        page.input_main_wrapper.send_keys(text_cockicock)
        page.btn_search_domain.click(1)

        time.sleep(10)
        print(page.group_valid_domain.get_text())
        check.not_equal(page.group_valid_domain.get_text().find(f'{text_cockicock+text_by_zone}'), -1)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки адреса ссылок')
def test_link_main(web_browser):
    """Этот тест проверяет адрес ссылок в кнопках """

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.btn_domain_link.is_clickable())
        check.is_true(page.btn_domain_link.is_visible())
        check.equal(page.btn_domain_link.get_attribute('href'), 'https://belavia.by/buy/')


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки количества плиток в блоке "Подберите свое решение"')
def test_count_box_main(web_browser):
    """Этот тест проверяет количество плиток в блоке "Подберите свое решение" """

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка количества плиток'):
        count = page.btn_count_box
        number = [(4), (9), (10), (3), (1), (4), (11), (3), (5), (53)]

        for count_elements in count:
            count_elements.click()
            check.equal(page.count_box.count(), number)

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class TestBelAvia(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://belavia.by/menu#")

    def test_menu(self):
        driver = self.driver
        menu_items = driver.find_elements_by_css_selector(".menu-list li")

        for item in menu_items:
            ActionChains(driver).move_to_element(item).perform()
            sub_menu = item.find_elements_by_css_selector(".submenu-list li")

            for sub_item in sub_menu:
                ActionChains(driver).move_to_element(sub_item).perform()
                time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

# Открытие страницы
driver.get("https://belavia.by/buttons")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "doubleClickBtn")))

# Нахождение элементов на странице
single_click_btn = driver.find_element(By.ID, "singleClickBtn")
double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
right_click_btn = driver.find_element(By.ID, "rightClickBtn")

# Нажатие на кнопки
single_click_btn.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))

action = webdriver.ActionChains(driver)
action.double_click(double_click_btn).perform()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))

action.context_click(right_click_btn).perform()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rightClickMessage")))

# Закрытие браузера
driver.quit()

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
