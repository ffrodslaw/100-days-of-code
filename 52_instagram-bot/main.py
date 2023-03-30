######
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Credentials

CHROME_DRIVER_PATH = "/home/anna/Applications/chromedriver"
USERNAME = os.environ["ig_username"]
PASSWORD = os.environ["ig_password"]

target_account = "buzzfeedtasty"

# chrome options
options = Options()
options.add_experimental_option("detach", True)


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
        # driver.maximize_window()

    def login(self):
        self.driver.get("http://www.instagram.com")
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        self.driver.get(f"http://www.instagram.com/{target_account}/followers")
        # followers = self.driver.find_elements(By.CSS_SELECTOR, '.x78zum5 li')
        # followers[1].click()
        # time.sleep(20)
        # pop_up = self.driver.find_element(By.CSS_SELECTOR, 'div[class="_aano"]')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
        sleep(10)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button[class="_acan _acap _acas"]')
        for button in follow_buttons:
            try:
                button.click()
            except:
                pass
        print("Bot successful.")


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
