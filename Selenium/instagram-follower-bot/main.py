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
account="calebpressley"


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.get("https://www.instagram.com/")
sleep(3)

username_input = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
username_input.send_keys(INSTAGRAM_EMAIL)
sleep(1)

password_input = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
password_input.send_keys(INSTAGRAM_PASSWORD)
password_input.send_keys(Keys.ENTER)
sleep(3)

search_button = dr



