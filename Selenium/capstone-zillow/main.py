import requests
from bs4 import BeautifulSoup
from pprint import pprint
from dotenv import load_dotenv
from time import sleep
import os

#load environment variables
load_dotenv()

class ZillowBot:

    def __init__(self,forms_url,zillow_url):
        self.forms_url = forms_url
        self.zillow_url  = zillow_url

    def getListingDetails(self):
        response = requests.get(self.zillow_url)
        soup = BeautifulSoup(response.text, "lxml")

        listings = soup.find(name="ul",class_="List-c11n-8-84-3-photo-cards").find_all("li")

        # listings_details=[]
        # for listing in listings:
        #     address =


        pprint(listings[0].getText())


#instantiate class and call methods to get details
ZILLOW_URL="https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORMS_URL = os.environ.get("GOOGLE_FORM_LINK")

zillow_bot = ZillowBot(GOOGLE_FORMS_URL,ZILLOW_URL)

zillow_bot.getListingDetails()