from selenium.webdriver.common.by import By
from assignment1_using_oop.pages.base_page import BasePage


class HomePage(BasePage):
    home_page_url = "https://evaly.com.bd/"
    banner_locator = (By.XPATH, "/html/body/reach-portal[1]/div/div/div/section/div/button")
    login_icon_locator = (By.XPATH, "//button[@class='flex items-center']")
    phone_no_locator = (By.XPATH, "//*//form//div[1]//label//input")
    password_locator = (By.XPATH, "//*//form//div[2]//label//input")
    login_button_locator = (By.XPATH, "//*//form//div[3]//button")
    phone_no = "01690217292"
    password = "@01690217292"

    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(self.home_page_url)
        self.do_click(self.banner_locator)

    def do_login(self):
        self.do_click(self.login_icon_locator)
        self.send_keys(self.phone_no_locator, self.phone_no)
        self.send_keys(self.password_locator, self.password)
        self.press_button(self.login_button_locator)


obj = HomePage()
obj.do_login()
