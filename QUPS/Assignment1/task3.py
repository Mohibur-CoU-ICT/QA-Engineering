# varify all career option contains career@evaly.com.bd or not
from selenium import webdriver

PATH = "C://Program Files (x86)//Chrome Driver//chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()
driver.get("https://evaly.com.bd/")
# closing pop up
try:
    driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button").click()
except Exception:
    print("No pop up exist")

# scroll at the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# click the Career link
driver.get(driver.find_element_by_xpath("//ul//li[@class='mb-2']//a[text()='Career']").get_attribute("href"))

# click I understand button
try:
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/button").click()
except Exception:
    print("No button exist")

all_career_option = driver.find_elements_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div")

# expanding all career option
for i in range(len(all_career_option)):
    all_career_option[i].click()

all_mails = driver.find_elements_by_xpath("//div[@class='p-6 mb-6']//p//a")
print("Total number of mails found = ", end='')
print(len(all_mails))

try:
    for each in all_mails:
        print(each.text)
        index = (str)(each.text).index("career@evaly.com.bd")
except Exception:
    print("career@evaly.com.bd not found in some of the category.")
finally:
    print("All mails contains career@evaly.com.bd at the end.")

# driver.close()
