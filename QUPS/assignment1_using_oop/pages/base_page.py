from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    CHROME_EXECUTABLE_PATH = "C://Program Files (x86)//Chrome Driver//chromedriver.exe"
    CHROME_OPTIONS = webdriver.ChromeOptions()
    CHROME_OPTIONS.add_argument("--disable-notifications")
    driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH, options=CHROME_OPTIONS)

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def press_button(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_link(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def is_enables(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def is_not_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)
