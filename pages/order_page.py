import time
import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Order_page(Base):
    """Страница оформления заказа"""

    # Faker Library Variables

    fake = Faker()
    phone_random = fake.phone_number()
    index_random = fake.postcode()
    address_random = fake.address()

    # Locators

    close_messenger = "jivo_close_button"
    pick_up_myself = "//div[contains(text(),'Самовывоз')]"
    name_field = "soa-property-1"
    email_field = "soa-property-2"
    phone_field = "(//input[@id='soa-property-3'])[2]"
    index_field = "soa-property-4"
    address_field = "soa-property-7"
    place_an_order = "//*[@id='bx-soa-orderSave']/a"

    # Getters

    def get_shipping_method(self):
        """Получение radio button Самовывоз"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_myself)))

    def get_phone_field(self):
        """Получение поля ввода номера телефона"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_address_field(self):
        """Получение поля ввода адреса"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.address_field)))

    # Actions

    def click_shipping_method(self):
        """Выбор способа доставки Самовывоз"""
        self.get_shipping_method().click()
        print("Click shipping method")
        self.driver.execute_script("window.scrollTo(0, 850)")

    def input_phone_field(self):
        """Ввод рандомного номера телефона"""
        self.get_phone_field().send_keys(self.phone_random)
        print("Input phone field")

    def input_address_field(self):
        """Ввод рандомного адреса"""
        self.get_address_field().send_keys(self.address_random)
        print("Input address field")

    def scroll_down(self):
        """Скролл страницы вниз"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    # Methods

    def input_shipping_information(self):
        with allure.step("Input shipping information"):
            Logger.add_start_step(method="input_shipping_information")
            self.click_shipping_method()
            time.sleep(2)
            self.input_phone_field()
            self.input_address_field()
            self.scroll_down()
            time.sleep(2)
            self.get_screenshot()  # Создание скриншота финального товара в корзине
            Logger.add_end_step(url=self.driver.current_url, method="input_shipping_information")
