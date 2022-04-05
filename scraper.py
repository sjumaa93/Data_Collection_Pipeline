from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome


class Scraper:
    def __init__(self, url, options=None):
        self.url = url
        if options:
            self.driver = Chrome('./chromedriver', options = options)
        else:
            self.driver = Chrome('./chromedriver')
        self.driver.get(url)

    def accept_cookies(self, xpath):
        cookies_button = self.driver.find_element(By.XPATH, xpath)
        cookies_button.click()

    def search_site(self, xpath, query):
        searchbox = self.driver.find_element(By.XPATH, xpath)
        searchbox.send_keys(query)
        searchbox.click()
        

    def clickgo(self,xpath):
        go_button = self.driver.find_element(By.XPATH, xpath)
        go_button.click()

    # def findproducts(self,xpath):
    #     elements = self.driver.find_element(By.XPATH, xpath)
    #     self.phone = [elements]
    #     for phone in elements




