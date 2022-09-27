# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import my_secrets

# Global constants
SPEEDTEST_URL = "https://fast.com/"


# Create an internet-speedtest-bot class for data collection | selenium
class SpeedtestBot:
    def __init__(self):
        # Create selenium chrome driver
        self.service = Service(executable_path=my_secrets.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        # Create parameters for download speed, upload speed and internet provider
        self.down = 0
        self.up = 0
        self.provider = None

    def run_speedtest(self):
        """Performs an internet speedtest using selenium chrome driver and saves download speed, upload speed,
        and current internet provider"""
        # Go to speedtest webpage
        self.driver.get(SPEEDTEST_URL)
        # Get download speed
        download_speed = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='speed-results-container succeeded']"))
        )
        # Convert download speed to Mbps if given in Kbps
        download_unit = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='speed-units-container succeeded']"))
        )
        if download_unit.text == "Kbps":
            self.down = round(float(download_speed.text) / 1000, 1)
        else:
            self.down = round(float(download_speed.text), 1)
        # Get upload speed
        more_info_button = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "//a[@id='show-more-details-link']"))
        )
        more_info_button.click()
        upload_speed = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='extra-measurement-value-container succeeded'][@id='upload-value']"))
        )
        # Convert upload speed to Mbps if given in Kbps
        upload_unit = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class=' succeeded'][@id='upload-units']"))
        )
        if upload_unit.text == "Kbps":
            self.up = round(float(upload_speed.text) / 1000, 1)
        else:
            self.up = round(float(upload_speed.text), 1)
        # Get current internet provider
        internet_provider = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@id='user-isp']"))
        )
        self.provider = internet_provider.text
