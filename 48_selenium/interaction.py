from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# options to stop Selenium from closing automatically
options = Options()
options.add_experimental_option("detach", True)

chrome_driver_path = "/home/anna/Applications/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

article_no = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_no.text)

# click
# article_click = article_no.click()

# portals_click = driver.find_element(By.LINK_TEXT, "Content portals").click()

# enter word and send enter
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.close()