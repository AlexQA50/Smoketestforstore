import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):
    """Ввод логина, пароля и авторизация"""

    # Variables

    url = 'https://it-m.by/'
    user_name = "for_citylink_mail@mail.ru"
    password = "Hy3bauy^RUU3"

    # Locators

    enter_login_button = "//div[@class='wrap_icon inner-table-block person']"
    user_name_field = "USER_LOGIN_POPUP"
    password_field = "USER_PASSWORD_POPUP"
    enter_button = "//button[@name='Login1']"

    # Getters

    def get_enter_login_button(self):
        """Получение локатора кнопки входа авторизации"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_login_button)))

    def get_user_name_field(self):
        """Получение локатора поля ввода логина"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.user_name_field)))

    def get_password_field(self):
        """Получение локатора поля ввода пароля"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.password_field)))

    def get_enter_button(self):
        """Получение локатора кнопки Войти"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    # Actions

    def click_enter_login_button(self):
        """Клик на кнопку входа авторизации"""
        self.get_enter_login_button().click()
        print("Click enter login button")

    def input_user_name(self):
        """Ввод логина пользователя"""
        self.get_user_name_field().send_keys(self.user_name)
        print("Input user name")

    def input_password(self):
        """Ввод пароля пользователя"""
        self.get_password_field().send_keys(self.password)
        print("Input password")

    def click_enter_button(self):
        """Клик на кнопку входа подтверждения авторизации"""
        self.get_enter_button().click()
        print("Click enter button")
        time.sleep(1)
        self.get_current_url()
        self.assert_url("https://it-m.by/")
        print("Authorization was successful!!!")

    # Methods

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_enter_login_button()
            self.input_user_name()
            self.input_password()
            self.click_enter_button()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
