import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Catalog_page(Base):
    """Главная страница каталого"""

    # Locators

    monitors_button = "(//span[@class='font_md'])[6]"

    # Getters

    def get_monitors_catalog(self):
        """Получение локатора кнопки Мониторы"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.monitors_button)))

    # Actions

    def click_monitors_catalog_button(self):
        """Клик кнопки Мониторы"""
        self.get_monitors_catalog().click()
        print("Click monitors catalog button")

    # Methods

    def select_monitors_catalog(self):
        with allure.step("Select monitors catalog"):
            Logger.add_start_step(method="select_monitors_catalog")
            self.click_monitors_catalog_button()
            time.sleep(2)
            Logger.add_end_step(url=self.driver.current_url, method="select_monitors_catalog")
