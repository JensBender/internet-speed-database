# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import my_secrets

# Global constants
TWITTER_URL = "https://twitter.com/i/flow/login"

# Create selenium chrome driver
service = Service(executable_path=my_secrets.CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
# Go to twitter login page
driver.get(TWITTER_URL)
# Enter email
email_input = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']"))
)
email_input.send_keys(my_secrets.TWITTER_EMAIL)
email_input.send_keys(Keys.ENTER)
time.sleep(2)
# Enter username
actions = ActionChains(driver)
actions.send_keys(my_secrets.TWITTER_USERNAME)
actions.perform()
actions.send_keys(Keys.ENTER)
actions.perform()
# Enter password
password_input = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
)
password_input.send_keys(my_secrets.TWITTER_PASSWORD)
password_input.send_keys(Keys.ENTER)
# Tweet complaint
tweet = f"Hey internet provider, why is my internet speed 9 download/ 9 upload" \
        f" when I pay for {my_secrets.PROMISED_DOWNLOAD} download/ {my_secrets.PROMISED_UPLOAD} upload?" \
        f" This is not an isolated case, but the average speed across 9 speedtest."
tweet_input = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Text twittern']"))
)
tweet_input.send_keys(tweet)
tweet_button = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Twittern']"))
)
tweet_button.click()
