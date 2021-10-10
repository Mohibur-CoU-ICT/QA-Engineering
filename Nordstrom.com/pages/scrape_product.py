from pages.base_page import BasePage


class Scrape(BasePage):
    def __init__(self):
        super().__init__(self.driver)

    def search_product(self):
        self.do_click(self.search_button_locator)
        self.send_keys(self.search_box_locator, "Fave Slipper")


obj = Scrape()
obj.search_product()
