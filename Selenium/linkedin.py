from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


linkedIn_email = ""
linkedIn_passowrd = ""
chrome_driver_path = "/Users/frederickt/Drivers/chromedriver"
chrome_service = Service(chrome_driver_path)

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search?keywords=software%2Bdeveloper&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=3758725433&position=1&pageNum=0")
time.sleep(3)

sign_in_button = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign in")
sign_in_button.click()
time.sleep(2)

username_input = driver.find_element(By.ID,"username")
username_input.send_keys(linkedIn_email)

password_input = driver.find_element(By.ID,"password")
password_input.send_keys(linkedIn_passowrd)
password_input.send_keys(Keys.ENTER)

time.sleep(15)

driver.quit()