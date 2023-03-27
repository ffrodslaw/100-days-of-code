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

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

fields = driver.find_elements(By.CSS_SELECTOR, ".form-signin input")
fname = fields[0]
lname = fields[1]
email = fields[2]

fname.send_keys("This")
lname.send_keys("is a")
email.send_keys("test@email.com")

button = driver.find_element(By.CSS_SELECTOR, "button")
button.send_keys(Keys.ENTER)

# driver.close()