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

        #get lisings ul and li from that
        listings_ul = soup.find(name="ul",class_="List-c11n-8-84-3-photo-cards")
        listings_li = listings_ul.find_all(name="li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

        #loop to get details from list
        listings_details=[]
        for listing in listings_li:
            listing_address = listing.find('address').text.strip()
            listing_url = listing.find('a').get('href')
            listing_price = listing.find('span',attrs={'data-test': 'property-card-price'}).getText().strip()
            listing_price_cleaned = listing_price[:6]
            listings_details.append([listing_address,listing_url,listing_price_cleaned])

        pprint(listings_details)


#instantiate class and call methods to get details
ZILLOW_URL="https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORMS_URL = os.environ.get("GOOGLE_FORM_LINK")

zillow_bot = ZillowBot(GOOGLE_FORMS_URL,ZILLOW_URL)

zillow_bot.getListingDetails()