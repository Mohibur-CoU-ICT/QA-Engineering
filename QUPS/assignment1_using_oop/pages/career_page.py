from selenium.webdriver.common.by import By
from assignment1_using_oop.pages.base_page import BasePage


class CareerPage(BasePage):
    career_page_url = "https://evaly.com.bd/career"
    banner_locator = (By.XPATH, "/html/body/reach-portal[1]/div/div/div/section/div/button")
    cookie_locator = (By.XPATH, "//*[@id='__next']/div[2]/div/button")
    career_page_locator = (By.XPATH, "//ul//li[@class='mb-2']//a[text()='Career']")
    all_career_option_locator = (By.XPATH, "//div//div//h3[@class='mb-0 font-semibold']")
    all_mails_locator = (By.XPATH, "//div[@class='p-6 mb-6']//p//a")

    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(self.career_page_url)
        # self.driver.get(self.driver.find_element(self.career_page_locator)).get_attribute("href")
        self.do_click(self.banner_locator)
        self.do_click(self.cookie_locator)

    def verify_all_career_has_formatted_mail_or_not(self):
        # Question no : 1
        all_career_option = self.driver.find_elements(*self.all_career_option_locator)  # option 1
        # all_career_option = self.driver.find_elements(By.XPATH, "//div//div//h3[@class='mb-0 font-semibold']") # option 2

        print("len of all_career_option = ", end="")
        print(len(all_career_option))

        # expanding all career option
        for i in range(len(all_career_option)):
            # Question no : 2
            # s = "//div//div[3]//div//div[2]//div[1]//div[{0}]".format(i + 1)
            # loc = (By.XPATH, s)
            # print(s)
            # print(loc)
            # self.do_click(loc)  # option 1
            all_career_option[i].click() # option 2

        # Question no : 3
        all_mails = self.driver.find_elements(*self.all_mails_locator)  # option 1
        # all_mails = self.driver.find_elements(By.XPATH, "//div[@class='p-6 mb-6']//p//a") # option 2
        print("Total number of mails found = ", end='')
        print(len(all_mails))

        try:
            for each in all_mails:
                print(each.text)
                index = str(each.text).index("career@evaly.com.bd")
            print("All mails contains career@evaly.com.bd at the end.")
        except Exception:
            print("career@evaly.com.bd not found in some of the category.")


obj = CareerPage()
obj.verify_all_career_has_formatted_mail_or_not()
