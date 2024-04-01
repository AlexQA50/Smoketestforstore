from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure


class Basket_page(Base):
    """Страница корзины"""

    # Locators

    place_an_order_button = "//button[contains(text(),'Оформить заказ')]"
    price_total = "//div[@class='basket-checkout-block-total-price-inner']"

    # Getters

    def get_price_total(self):
        """Получение локатора поля Итого"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_total)))

    def get_place_an_order_button(self):
        """Получение локатора кнопки Оформить заказ"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.place_an_order_button)))

    # Actions

    def price_total_for_assert_funk(self):
        """Удаление из цены элемента руб. и внесение в переменную для сверки assert"""
        global price_total_for_assert
        price_total_for_assert = self.get_price_total().text.replace(" руб.", "")
        print(f"Price total for assert is: {price_total_for_assert}")
        return price_total_for_assert

    def click_place_an_order(self):
        """Клик на кнопку оформление заказа"""
        self.get_place_an_order_button().click()
        print("Clicking the order registration button")

    # Methods

    def click_place(self):
        with allure.step("Click place"):
            Logger.add_start_step(method="click_place")
            print("The price is checked and correct with the price in the catalog")
            self.click_place_an_order()
            Logger.add_end_step(url=self.driver.current_url, method="click_place")
