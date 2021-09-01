# task 1: login to evaly.com.bd
from selenium import webdriver

PATH = "C://Program Files (x86)//Chrome Driver//chromedriver.exe"
driver = webdriver.Chrome(PATH)

# maximize the browser
driver.maximize_window()
# loading home page
driver.get("https://evaly.com.bd/")

# closing pop-up
try:
    # close the banner
    driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button").click()
    # click I understand button
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/button").click()
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

# fill password
driver.find_element_by_xpath("//*//form//div[2]//label//input").send_keys("@01690217292")

# click login button
driver.find_element_by_xpath("//*//form//div[3]//button").click()


# task 2: printing all brands name
driver.implicitly_wait(5)

# loading speaker page
driver.get(driver.find_element_by_xpath("//li[9]//a[@class='flex items-center justify-between py-3 text-sm ']").get_attribute("href"))

# getting all brands
brands_links = driver.find_elements_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div/div/div/a")

print("Total number of brands = ", end='')
print(len(brands_links))

# printing all brands names
for i in range(len(brands_links)):
    print(brands_links[i].text)
    # print( + " " + (str)(brands_links[i].get_attribute("href")))

# loading mi page
driver.get(brands_links[0].get_attribute("href"))

# getting all mi products
mi_products = driver.find_elements_by_xpath("//div[@class='slug__Grid-sc-vcgsbx-0 hOwKLS pb-24 my-4 md:pb-4']//a")

print("Total number of products in MI = ", end='')
print(len(mi_products))

mx_price = 0
for i in range(len(mi_products)):
    index = str(i+1)
    print("index = ", end='')
    print(index)

    title = driver.find_element_by_xpath("//*//a["+index+"]//div//div[@class='px-4 py-2']//p").text
    price = driver.find_element_by_xpath("//*//a["+index+"]//div//div[@class='p-4 pt-0']//p").text
    int_price = int(str(price).replace("৳", ""))

    if int_price > mx_price:
        mx_price = int_price

    # loading ith product page
    driver.get(driver.find_element_by_xpath("//div[@class='container m-auto']//div//a["+index+"]").get_attribute("href"))

    new_title = driver.find_element_by_xpath("//div//h2[@class='font-bold text-gray-700']").text
    new_price = driver.find_element_by_xpath("//h2[@class='flex items-start mb-0 font-bold leading-none text-gray-800']").text
    new_price = str(new_price).replace(" ", "")

    if not str(price).endswith(".00"):
        price = price + ".00"

    print(title + "\n" + new_title)
    print(price + "\n" + new_price)

    assert str(title).strip() == str(new_title).strip() # removing leading and trainling whitespaces
    assert str(price) == str(new_price)

    driver.execute_script("window.history.go(-1)")

print("Maximum price = ", end='')
print(mx_price, end='\n\n')


# task 3: varify all career option contains career@evaly.com.bd or not
driver.implicitly_wait(5)

# scroll at the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# click the Career link
driver.get(driver.find_element_by_xpath("//ul//li[@class='mb-2']//a[text()='Career']").get_attribute("href"))

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
    print("All mails contains career@evaly.com.bd at the end.")
except Exception:
    print("career@evaly.com.bd not found in some of the category.")

driver.implicitly_wait(5)
driver.close()
