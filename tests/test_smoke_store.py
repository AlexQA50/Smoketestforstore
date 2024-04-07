from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pages.catalog_page import Catalog_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.monitors_page import Monitors_page
from pages.order_page import Order_page
from pages.product_page import Product_page
from base.base_class import Base
from pages.basket_page import Basket_page


@allure.description("Test smoke")
def test_smoke(start_and_finish):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start Test 1!")

    login = Login_page(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_main_catalog()

    catalog_page = Catalog_page(driver)
    catalog_page.select_monitors_catalog()

    monitors_page = Monitors_page(driver)
    monitors_page.select_iiyama_catalog()

    product_page = Product_page(driver)
    ppp = product_page.get_product_price_for_check()
    print(ppp)
    product_page.check_product_and_add_to_cart()

    basket_page = Basket_page(driver)
    bpp = basket_page.price_total_for_assert_funk()
    print(bpp)
    basket_page.click_place()
    base = Base(driver)
    base.assert_price(bpp, ppp)

    order_page = Order_page(driver)
    order_page.input_shipping_information()
