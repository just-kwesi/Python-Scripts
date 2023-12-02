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

        start_button = self.driver.find_element(By.CSS_SELECTOR,".start-button a")
        start_button.click()

        sleep(45)

        self.down = self.driver.find_element(By.CSS_SELECTOR, ".result-data .download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".result-data .upload-speed").text
        # print(f"download speed = {self.down} upload speed={self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        sleep(2)

        email_input = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(X_EMAIL)
        email_input.send_keys(Keys.ENTER)
        sleep(2)

        suspicios_activity = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        suspicios_activity.send_keys("python_bot_101")
        suspicios_activity.send_keys(Keys.ENTER)
        sleep(2)

        # password_input = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')

        password_input.send_keys(X_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        sleep(3)





bot = InternetSpeedTwitterBot(chrome_service,chrome_options)
# bot.get_internet_speed()
bot.tweet_at_provider()





