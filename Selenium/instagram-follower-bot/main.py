from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
load_dotenv()

chrome_driver_path = "/Users/frederickt/Drivers/chromedriver"
chrome_service = Service(chrome_driver_path)

#instagram credentials
INSTAGRAM_EMAIL = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")
account="calebwsimpson"


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)


search_button = driver.find_element(By.XPATH,'//*[@id="mount_0_0_l3"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div/svg')
search_button.click()
sleep(1)

search_bar = driver.find_element(By.XPATH,'//*[@id="mount_0_0_gi"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
search_bar.send_keys(account)
sleep(2)

first_result = driver.find_element(By.XPATH,'//*[@id="mount_0_0_gi"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/div/span')
first_result.click()
sleep(3)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(3)

        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(INSTAGRAM_EMAIL)
        sleep(1)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(INSTAGRAM_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        sleep(5)


