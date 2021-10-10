import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    CHROME_EXECUTABLE_PATH = "C://Program Files (x86)//Chrome Driver//chromedriver.exe"
    CHROME_OPTIONS = webdriver.ChromeOptions()
    CHROME_OPTIONS.add_argument("--disable-notifications")
    BASE_URL = "https://www.nordstrom.com/"
    driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH, options=CHROME_OPTIONS)
    workbook_path = "E:\\Python\\Nordstrom.com\\product_details.xlsx"
    # locators
    search_button_locator = "//a[@id='controls-keyword-search-popover']"
    search_box_locator = "//*[@id='keyword-search-input']"
    # variables
    short_delay = 3  # depends on internet speed
    medium_delay = 10

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)
        time.sleep(self.medium_delay)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def is_enables(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)
