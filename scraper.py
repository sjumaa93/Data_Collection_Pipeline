from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
import time


class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = Chrome('./chromedriver')
        self.driver.get(url)

    def accept_cookies(self, xpath):
        time.sleep(1)
        self.driver.find_element(By.XPATH, xpath).click()

    def search_site(self, xpath, query):
        time.sleep(1)
        searchbox = self.driver.find_element(By.XPATH, xpath)
        searchbox.send_keys(query)
        searchbox.click()

    def go_button(self,xpath):
        time.sleep(1)
        self.driver.find_element(By.XPATH, xpath).click()

    def findproducts(self,xpath):
        time.sleep(5)
        myphone=[]
        product_name = self.driver.find_elements(By.XPATH, xpath)
        for title in product_name:
            myphone.append(title.text)
        print(myphone)



