# login to evaly.com.bd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

PATH = "C://Program Files (x86)//Chrome Driver//chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()
driver.get("https://evaly.com.bd/")
print("Page title = " + driver.title)

# closing pop-up
try:
    driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button").click()
except Exception:
    print("No pop up exist")

# click into the login icon
driver.find_element_by_xpath("//button[@class='flex items-center']").click()

"""most important statement for this program
without this statement this program may ot work
we have to wait for some time to get the accurate xpath
for phone number and password field and to click LOGIN button"""
driver.implicitly_wait(5)

# fill-up login form
# fill phone number)
driver.find_element_by_xpath("//*//form//div[1]//label//input").send_keys("01690217292")
# driver.find_element(By.NAME, "phone").send_keys("01690217292")

# fill password
driver.find_element_by_xpath("//*//form//div[2]//label//input").send_keys("@01690217292")
# driver.find_element(By.NAME, "password").send_keys("@01690217292")

# click login button
driver.find_element_by_xpath("//*//form//div[3]//button").click()

# driver.implicitly_wait(30)
# driver.close()
