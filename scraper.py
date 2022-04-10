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

    def click_go_button(self,xpath):
        time.sleep(1)
        self.driver.find_element(By.XPATH, xpath).click()

    def find_links(self, xp_html, xp_price, xp_title):
        time.sleep(2)
        link_list = []
        container = self.driver.find_elements(By.XPATH, xp_html)
        for link in container:
            link_list.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        
        print(link_list)
        
        dict_list = {
            'Link':[],
            'Name':[],
            'Price':[]
            }
        for link in link_list[0:4]:
            self.driver.get(link)
            time.sleep(2)
            dict_list['Link'].append(link)
            price = self.driver.find_element(By.XPATH, xp_price)
            dict_list['Price'].append(price)
            name = self.driver.find_element(By.XPATH, xp_title)
            dict_list['Name'].append(name)
        
        print(dict_list)

    def close_driver(self):
        self.driver.quit()


    #def find_product_title(self,xpath):
    #    time.sleep(5)
    #    link_list=[]
    #    product_name = self.driver.find_element(By.XPATH, xpath).__getattribute__('href')
    #    for title in product_name:
    #        link_list.append(title.text)
    #    print(link_list)

    #def find_product_title(self, xpath):
    #    self.container = self.driver.find_element(By.XPATH, xpath)


    # div container - div class = "a-section a-spacing-none s-padding-right-small s-title-instructions-style"