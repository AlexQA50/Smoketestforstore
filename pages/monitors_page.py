import time
import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from base.base_class import Base
from utilities.logger import Logger
from selenium.common.exceptions import NoSuchElementException


class Monitors_page(Base):
    """Главная страница мониторов"""

    # Locators

    iiyama = "(//span[contains(text(), 'iiyama')])[2]"
    select_diagonal = "//span[contains(text(),'Диагональ')]"
    min_price = "MAX_SMART_FILTER_6625_MIN"
    max_price = "MAX_SMART_FILTER_6625_MAX"
    body_color_button = "(//span[contains(text(),'Цвет корпуса')])[1]"
    white_color_body = "(//span[@title='белый'])[2]"
    selected_product_1 = "//div[@class='inner_wrap TYPE_1']"
    move_to_product_page_locator = "//a[@class='dark_link js-notice-block__title option-font-bold font_sm']"
    monitor_price = "//span[@class='values_wrapper']"

    # Variables

    min_price_value = 27
    max_price_value = 27
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

    # Getters

    def get_iiyama_catalog(self):
        """Получение локатора кнопки iiyama"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iiyama)))

    def get_diagonal(self):
        """Получение локатора кнопки Диагональ"""
        return WebDriverWait(self.driver, 30, ignored_exceptions=self.ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, self.select_diagonal)))

    def get_min_price(self):
        """Получение локатора поля Минимальная диагональ"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.min_price)))

    def get_max_price(self):
        """Получение локатора поля Максимальная диагональ"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.max_price)))

    def get_body_color_button(self):
        """Получение локатора кнопки цвета корпуса"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.body_color_button)))

    def get_white_color_body(self):
        """Получение локатора белого цвета корпуса"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.white_color_body)))

    def get_selected_product_1_field(self):
        """Получение локатора поля товара для появления кнопки В корзину"""
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.selected_product_1)))

    def add_move_to_product_page_button(self):
        """Получение локатора кнопки В корзину"""
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.move_to_product_page_locator)))

    # Actions

    def click_iiyama_catalog_button(self):
        """Клик кнопки iiyama"""
        self.get_iiyama_catalog().click()
        print("Click iiyama catalog button")

    def click_diagonal_button(self):
        self.get_diagonal().click()
        print("Click diagonal button")

    def send_min_price(self):
        """Ввод минимальной диагонали """
        self.get_min_price().send_keys(self.min_price_value)
        print("Sent min diagonal")

    def send_max_price(self):
        """Ввод максимальной диагонали """
        self.get_max_price().send_keys(self.max_price_value)
        print("Sent max diagonal")

    # def click_body_color_button_button(self):
    #     """Клик кнопки Цвет корпуса"""
    #     self.get_body_color_button().click()
    #     print("Click body_color_button")
    #
    # def click_white_color_body(self):
    #     """Клик кнопки белого цвета корпуса"""
    #     self.get_white_color_body().click()
    #     print("Click white_color_body")

    def move_to_selected_product_1_field(self):
        """Наведение мыши на поле товара для появления кнопки В корзину.
        Возможна ошибка StaleElementReferenceException потому через Try"""
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.get_selected_product_1_field()).perform()
            print("Click selected_product_1_field")

        except StaleElementReferenceException:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.get_selected_product_1_field()).perform()
            print("Was StaleElementReferenceException")

    def click_move_to_product_page(self):
        """Скролл страницы вниз и клик кнопки В корзину.
        Возможна ошибка StaleElementReferenceException потому через Try"""
        try:
            self.driver.execute_script("window.scrollTo(0, 200)")
            time.sleep(2)
            self.add_move_to_product_page_button().click()
            print("Click move to product page")

        except StaleElementReferenceException:
            self.driver.execute_script("window.scrollTo(0, 200)")
            time.sleep(2)
            self.add_move_to_product_page_button().click()
            print("Was StaleElementReferenceException")

    # Methods

    def select_iiyama_catalog(self):
        with allure.step("Select iiyama catalog"):
            Logger.add_start_step(method="select_iiyama_catalog")
            self.click_iiyama_catalog_button()
            time.sleep(2)
            self.click_diagonal_button()
            time.sleep(1)
            self.send_min_price()
            time.sleep(1)
            self.send_max_price()
            time.sleep(1)
            # self.click_body_color_button_button()
            # time.sleep(1)
            # self.click_white_color_body()
            # time.sleep(1)
            self.move_to_selected_product_1_field()
            time.sleep(1)
            self.click_move_to_product_page()
            Logger.add_end_step(url=self.driver.current_url, method="select_iiyama_catalog")
