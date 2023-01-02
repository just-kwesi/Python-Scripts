from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/frederickt/Drivers/chromedriver"
chrome_service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service)

driver.get("https://www.amazon.com/")

amazon_search = driver.find_element(By.ID, "twotabsearchtextbox")
amazon_search.send_keys("digital scale")
amazon_search.send_keys(Keys.ENTER)

