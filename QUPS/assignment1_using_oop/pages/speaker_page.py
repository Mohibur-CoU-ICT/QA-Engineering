from selenium.webdriver.common.by import By
from assignment1_using_oop.pages.base_page import BasePage


class SpeakerPage(BasePage):
    banner_locator = (By.XPATH, "/html/body/reach-portal[1]/div/div/div/section/div/button")
    cookie_locator = (By.XPATH, "//*[@id='__next']/div[2]/div/button")
    speaker_page_url = "https://evaly.com.bd/categories/speaker-2f615cf9a"
    speaker_option_locator = (By.XPATH, "//li[9]//a[@class='flex items-center justify-between py-3 text-sm ']")
    brands_name_locator = (By.XPATH, "//div[@class='w-full my-4']//div//a")
    mi_products_locator = (By.XPATH, "//div[@class='slug__Grid-sc-vcgsbx-0 hOwKLS pb-24 my-4 md:pb-4']//a")

    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(self.speaker_page_url)
        self.do_click(self.banner_locator)
        self.do_click(self.cookie_locator)
        self.brands_links = self.driver.find_elements(*self.brands_name_locator)

    def goto_speaker_page(self):
        self.get_link(self.speaker_option_locator)
        # self.driver.get(self.driver.find_element(self.speaker_option_locator))
        # self.do_click(self.speaker_option_locator)

    def print_all_brands_names(self):
        for i in range(len(self.brands_links)):
            print(self.brands_links[i].text)

    def goto_mi_page(self):
        self.driver.get(self.brands_links[0].get_attribute("href"))

    def find_max_price_among_all_mi_products(self):
        mx_price = 0
        mi_products = self.driver.find_elements(*self.mi_products_locator)
        for i in range(len(mi_products)):
            index = str(i + 1)
            print("index = ", end='')
            print(index)

            title = self.driver.find_element_by_xpath("//*//a[" + index + "]//div//div[@class='px-4 py-2']//p").text
            price = self.driver.find_element_by_xpath("//*//a[" + index + "]//div//div[@class='p-4 pt-0']//p").text
            int_price = int(str(price).replace("৳", ""))

            if int_price > mx_price:
                mx_price = int_price

            # loading ith product page
            self.driver.get(self.driver.find_element_by_xpath(
                "//div[@class='container m-auto']//div//a[" + index + "]").get_attribute("href"))

            new_title = self.driver.find_element_by_xpath("//div//h2[@class='font-bold text-gray-700']").text
            new_price = self.driver.find_element_by_xpath(
                "//h2[@class='flex items-start mb-0 font-bold leading-none text-gray-800']").text
            new_price = str(new_price).replace(" ", "")

            if not str(price).endswith(".00"):
                price = price + ".00"

            print(title + "\n" + new_title)
            print(price + "\n" + new_price)

            # assert str(title).strip() == str(new_title).strip() # removing leading and trailing whitespaces
            # assert str(price) == str(new_price)

            self.driver.execute_script("window.history.go(-1)")

        return mx_price


obj = SpeakerPage()
# obj.goto_speaker_page()
obj.print_all_brands_names()
obj.goto_mi_page()
obj.find_max_price_among_all_mi_products()
