from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import os

load_dotenv()

chrome_driver_path = "/Users/frederickt/Drivers/chromedriver"
chrome_service = Service(chrome_driver_path)

#login details
X_EMAIL = os.environ.get("TWITTER_EMAIL")
X_PASSWORD = os.environ.get("TWITTER_PASSWORD")


print(f"{X_PASSWORD},{X_EMAIL}")
# Optional - Keep the browser open (helps diagnose issues if the script crashes)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach',True)
#
# driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
# driver.get("https://twitter.com/home")
# sleep(2)

