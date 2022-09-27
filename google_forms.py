# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import my_secrets


# Create a Google-forms-bot class for data entry | selenium
class GoogleFormsBot:
    def __init__(self):
        self.service = Service(executable_path=my_secrets.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def fill_out_form(self, download_speed, upload_speed, internet_provider):
        # Go to the (predefined) Google form
        self.driver.get(my_secrets.GOOGLE_FORM_URL)
        # Get all text input fields from the Google form
        input_fields = WebDriverWait(self.driver, 120).until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[@type='text']"))
        )
        # Fill in the information
        time.sleep(1)
        input_fields[0].send_keys(download_speed)
        input_fields[1].send_keys(upload_speed)
        input_fields[2].send_keys(internet_provider)
        # Click submit button
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Senden']"))
        ).click()
