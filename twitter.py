# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time
import data_analysis
import my_secrets

# Global constants
TWITTER_URL = "https://twitter.com/i/flow/login"


class TwitterBot:
    def __init__(self, down_up_df):
        self.service = Service(executable_path=my_secrets.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.speed_by_provider_df = down_up_df

    def tweet_complaint(self, internet_provider):
        # Go to twitter login page
        self.driver.get(TWITTER_URL)
        # Enter email
        email_input = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']"))
        )
        email_input.send_keys(my_secrets.TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(2)
        # Enter username
        actions = ActionChains(self.driver)
        actions.send_keys(my_secrets.TWITTER_USERNAME)
        actions.perform()
        actions.send_keys(Keys.ENTER)
        actions.perform()
        # Enter password
        password_input = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_input.send_keys(my_secrets.TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        # Get speedtest results
        download = self.speed_by_provider_df.loc[internet_provider]["Mean Download"]
        upload = self.speed_by_provider_df.loc[internet_provider]["Mean Upload"]
        n_speedtests = round(self.speed_by_provider_df.loc[internet_provider]["n"])
        # Tweet complaint
        tweet = f"Hey {internet_provider}, why is my internet speed {download}down/{upload}up" \
                f" when I pay for {my_secrets.PROMISED_DOWNLOAD}down/{my_secrets.PROMISED_UPLOAD}up?" \
                f" This is not an isolated case, it's the average internet speed from {n_speedtests} speedtests."
        tweet_input = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Text twittern']"))
        )
        tweet_input.send_keys(tweet)
        tweet_button = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Twittern']"))
        )
        try:
            tweet_button.click()
        except ElementClickInterceptedException:
            actions.send_keys(Keys.ESCAPE)
            actions.perform()
            tweet_button.click()


# Create a Twitter bot that prompts the user for a Twitter complaint
twitter_bot = TwitterBot(data_analysis.down_up_mean)
twitter_bot.tweet_complaint(internet_provider="AIS")
