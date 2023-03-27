from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# options to stop Selenium from closing automatically
options = Options()
options.add_experimental_option("detach", True)

chrome_driver_path = "/home/anna/Applications/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

driver.get("https://www.python.org")
search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("Placeholder"))

logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo)

doc_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(doc_link.text)

# XPath search
bug_link = driver.find_element(By.XPATH, '//*[@id="container"]/li[8]/ul/li[5]/a')
# print(bug_link.text)



### get events
times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# print(times.get_attributes("datetime"))

data = {i: {"time": times[i].get_attribute("datetime")[0:10], "name": events[i].text} for i in range(len(times)-1)}
print(data)


# driver.close() # for tab
driver.quit() # for browser