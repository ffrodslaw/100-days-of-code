from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# options to stop Selenium from closing automatically
# options = Options()
# options.add_experimental_option("detach", True)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

chrome_driver_path = "/home/anna/Applications/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

store = driver.find_elements(By.CSS_SELECTOR, "#store div")
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

upgrades = {int(store[i].text.split("-")[1].split("\n")[0].strip().replace(",", "")):store[i].get_attribute("id") for i in range(len(store)-1)}


def buy_most_expensive_item():
    money = int(driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", ""))
    can_buy = {}
    for price, id in upgrades.items():
        if money >= price:
            can_buy[price] = id
    id_to_buy = can_buy[max(can_buy)]
    print(id_to_buy)
    driver.find_element(By.ID, id_to_buy).click()

timeout = time.time() + 1
end = time.time() + 60*5
while True:
    cookie.click()
    # print(time.time() - timeout)
    if time.time() > end:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
    if time.time() > timeout:
        buy_most_expensive_item()
        timeout = time.time() + 5

driver.close()