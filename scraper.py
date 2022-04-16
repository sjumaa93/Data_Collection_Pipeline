from cgi import print_exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
#from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd
import uuid
import json

class Web_Scraper:

    def __init__(self, url):
        self.url = url
        #self.driver = Chrome(ChromeDriveManager().install())
        self.driver = Chrome('./chromedriver')
        self.driver.get(url)

    def accept_cookies(self, xpath):
        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH, xpath).click()
        except:
            print('No cookies found')

    def search_site(self, xpath, query):
        time.sleep(1)
        searchbox = self.driver.find_element(By.XPATH, xpath)
        searchbox.send_keys(query)
        searchbox.click()

    def click_go_button(self,xpath):
        time.sleep(1)
        self.driver.find_element(By.XPATH, xpath).click()


    def find_data(self, xp_html, xp_title, xp_price):
        time.sleep(2)
        link_list = []
        container = self.driver.find_elements(By.XPATH, xp_html)
        for link in container:
            link_list.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        
        dict_list = {
            'Link':[],
            'Name':[],
            'Price':[],
            'UUID':[],
            }

        for link in link_list[0:4]:
            self.driver.get(link)
            time.sleep(2)
            dict_list['Link'].append(link)
            name = self.driver.find_element(By.XPATH, xp_title).text
            dict_list['Name'].append(name)
            price = self.driver.find_element(By.XPATH, xp_price).text
            dict_list['Price'].append(price)
            #asin = self.driver.find_element(By.ID, xp_asin).text
            #dict_list['ASIN'].append(asin)
            id = uuid.uuid4()
            dict_list['UUID'].append(id)
        
        print(pd.DataFrame(dict_list))

        return dict_list
    
    def create_json(self):
        link_list = self.find_data()
        file = json.dumps(link_list)
        with open('file.json', 'w') as f:
            f.write(file)
            f.close()

    def close_driver(self):
        self.driver.quit()