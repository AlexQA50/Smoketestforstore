from datetime import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url is: " + get_url)

    # Method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Assert word is: " + value_word)

    # Method screenshot
    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d.  %H.%M.%S")
        name_screenshot = "screenshot_" + now_date + ".png"
        self.driver.save_screenshot("screen/" + name_screenshot)
        print(name_screenshot)

    # Method assert url
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Current url is correct: " + get_url)

    # Method assert price
    def assert_price(self, price, result):
        value_price = price
        assert value_price == result
        print("Assert price is: " + value_price)
