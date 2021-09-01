# printing all brands name
from selenium import webdriver

PATH = "C://Program Files (x86)//Chrome Driver//chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()
driver.get("https://evaly.com.bd/")

try:
    driver.find_element_by_xpath("//div//button[@class='absolute top-0 right-0 p-2 text-white']").click()
except Exception:
    print("No pop up exist")

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
i = 1
for i in range(len(mi_products)):
    index = str(i)
    print("index = ", end='')
    print(index)

    title = driver.find_element_by_xpath("//a["+index+"]//div//div[@class='px-4 py-2']//p").text
    price = driver.find_element_by_xpath("//a["+index+"]//div//div[@class='p-4 pt-0']//p").text
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
    i = i + 1

print("Maximum price = ", end='')
print(mx_price)

# driver.close()
