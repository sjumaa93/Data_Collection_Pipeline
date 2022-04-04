from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


from selenium.webdriver import Chrome
driver = Chrome('./chromedriver')

class Scraper:
    def __init__(self, url, options=None):
        self.url = url
        if options:
            self.driver = Chrome('./chromedriver', options = options)
        else:
            self.driver = Chrome('./chromedriver')

    def accept_cookies(self, xpath):
        cookies_button = self.driver.find_element(By.XPATH, xpath)
        cookies_button.click

    def search_site(self, xpath):
        pass


