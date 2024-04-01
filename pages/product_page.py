import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Product_page(Base):
    """Страница монитора iiyama"""

    # Locators

    locator = "//h1[@id='pagetitle']"
    price_value_locator = "(//span[@class='price_value'])[4]"
    add_to_basket = "//div[@id='bx_117848907_175133_basket_actions']"
    enter_to_basket = "(//span[@class='js-basket-block'])[3]"

    # Getters

    def get_product_price_for_assert(self):
        """Получение локатора цены товара для проверки"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_value_locator)))

    def get_add_to_basket_button(self):
        """Получение локатора цены товара для проверки"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_basket)))

    def get_enter_to_basket_button(self):
        """Получение локатора цены товара для проверки"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_to_basket)))

    # Actions

    def get_product_price_for_check(self):
        """Получение цены продукта для сверки assert и запись в файл"""
        global value_product_price
        value_product_price = self.get_product_price_for_assert().text
        print(value_product_price)
        return value_product_price

    def click_add_to_basket_button(self):
        """Добавление товара в корзину"""
        self.get_add_to_basket_button().click()
        print("The product has been added to the cart")

    def click_enter_to_basket_button(self):
        """Нажатие кнопки перехода в корзину"""
        self.get_enter_to_basket_button().click()
        print("Go to the shopping cart")

    # Methods

    def check_product_and_add_to_cart(self):
        with allure.step("Check product and add to cart"):
            Logger.add_start_step(method="check_product_and_add_to_cart")
            self.click_add_to_basket_button()
            self.click_enter_to_basket_button()
            Logger.add_end_step(url=self.driver.current_url, method="check_product_and_add_to_cart")
