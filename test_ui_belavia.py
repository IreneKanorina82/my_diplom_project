import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
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
