import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    """Главная страница"""

    # Locators

    catalog_button = "(//a[@class='dropdown-toggle'])[4]"
    main_word = 'pagetitle'

    # Getters
    def get_catalog(self):
        """Получение локатора кнопки каталога на главной странице"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_main_word(self):
        """Получение локатора проверочного слова"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.main_word)))

    # Actions
    def move_to_catalog_button(self):
        """Поиск кнопки Каталог на главной странице. Возможна ошибка StaleElementReferenceException потому через Try"""

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.get_catalog()).perform()
            print("Move to catalog button")
            self.get_catalog().click()
            print("Click catalog button")

        except StaleElementReferenceException:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.get_catalog()).perform()
            print("Was StaleElementReferenceException")
            self.get_catalog().click()
            print("Click catalog button")

    # Methods
    def select_main_catalog(self):
        with allure.step("Select main catalog"):
            Logger.add_start_step(method="select_main_catalog")
            self.move_to_catalog_button()
            self.assert_word(self.get_main_word(), 'Каталог')
            Logger.add_end_step(url=self.driver.current_url, method="select_main_catalog")
