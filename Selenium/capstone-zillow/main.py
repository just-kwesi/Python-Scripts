import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#load environment variables
load_dotenv()

class ZillowBot:

    def __init__(self,forms_url,zillow_url):
        chrome_driver_path = "/Users/frederickt/Drivers/chromedriver"
        chrome_service = Service(chrome_driver_path)

        # Optional - Keep the browser open (helps diagnose issues if the script crashes)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
        self.forms_url = forms_url
        self.zillow_url  = zillow_url
        self.listing_details=[]

    def getListingDetails(self):
        response = requests.get(self.zillow_url)
        soup = BeautifulSoup(response.text, "lxml")

        #get listings ul and li from that
        listings_ul = soup.find(name="ul",class_="List-c11n-8-84-3-photo-cards")
        listings_li = listings_ul.find_all(name="li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

        #loop to get details from list
        for listing in listings_li:
            listing_address = listing.find('address').text.strip()
            listing_url = listing.find('a').get('href')
            listing_price = listing.find('span',attrs={'data-test': 'property-card-price'}).getText().strip()
            listing_price_cleaned = listing_price[:6]
            self.listing_details.append([listing_address,listing_url,listing_price_cleaned])

    def writeDetailsToForm(self):
        self.driver.get(self.forms_url)
        sleep(2)

        for listing in self.listing_details:
            address_input = self.driver.find_element(By.XPATH,
                                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH,
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')


            address_input.send_keys(listing[0])
            price_input.send_keys(listing[1])
            link_input.send_keys(listing[2])
            submit_button.click()

            sleep(2)
            submit_again_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            submit_again_button.click()
            sleep(1)

        self.driver.quit()

        print(f"Listing details completed.")







#instantiate class and call methods to get details
ZILLOW_URL="https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORMS_URL = os.environ.get("GOOGLE_FORM_LINK")

zillow_bot = ZillowBot(GOOGLE_FORMS_URL,ZILLOW_URL)

zillow_bot.getListingDetails()
zillow_bot.writeDetailsToForm()