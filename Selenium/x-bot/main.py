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

#login details
X_EMAIL = os.environ.get("TWITTER_EMAIL")
X_PASSWORD = os.environ.get("TWITTER_PASSWORD")



# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)


class InternetSpeedTwitterBot:
    def __init__(self,driver_service,driver_options):
        self.driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(1)

        # start_button = self.driver.find_element(By.CSS_SELECTOR,".start-button a")

        start_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_button.click()

        sleep(20)



    def tweet_at_provider(self):
        print('tweeting')



bot = InternetSpeedTwitterBot(chrome_service,chrome_options)
bot.get_internet_speed()
bot.tweet_at_provider()




