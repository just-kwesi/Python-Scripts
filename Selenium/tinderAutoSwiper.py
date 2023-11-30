from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

from dotenv import load_dotenv
load_dotenv()

chrome_driver_path = "/Users/frederickt/Drivers/chromedriver"
chrome_service = Service(chrome_driver_path)

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.get("https://tinder.com/")
time.sleep(3)

sign_in_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
sign_in_button.click()