from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_EXECUTABLE_PATH = "C://Program Files (x86)//Chrome Driver//chromedriver.exe"
CHROME_OPTIONS = webdriver.ChromeOptions()
PROXY = "45.88.41.158:8080"
CHROME_OPTIONS.add_argument("start-maximized")
CHROME_OPTIONS.add_argument("--disable-notifications")
CHROME_OPTIONS.add_argument('--proxy-server=%s' % PROXY)
CHROME_OPTIONS.add_argument('--disable-blink-features')
CHROME_OPTIONS.add_argument('--disable-blink-features=AutomationControlled')
CHROME_OPTIONS.add_experimental_option("excludeSwitches", ["enable-automation"])
CHROME_OPTIONS.add_experimental_option('useAutomationExtension', False)
CHROME_OPTIONS.add_argument("--incognito")
BASE_URL = "https://www.nordstrom.com/"
driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH, options=CHROME_OPTIONS)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})


# locators
search_button_locator = "//a[@id='controls-keyword-search-popover']"
search_box_locator = "//*[@id='keyword-search-input']"

driver.get(BASE_URL)
driver.find_element(By.XPATH, search_button_locator)
driver.find_element(By.XPATH, search_box_locator).send_keys("Fave Slipper")
