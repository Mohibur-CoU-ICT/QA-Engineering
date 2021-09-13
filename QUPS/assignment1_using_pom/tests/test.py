from assignment1_using_pom.pages.career_page import CareerPage
from assignment1_using_pom.pages.home_page import HomePage
from assignment1_using_pom.pages.speaker_page import SpeakerPage


class Test:
    obj = HomePage()
    obj.do_login()
    obj = SpeakerPage()
    obj.print_all_brands_names()
    obj.goto_mi_page()
    obj.find_max_price_among_all_mi_products()
    obj = CareerPage()
    obj.verify_all_career_has_formatted_mail_or_not()

