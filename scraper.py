from cgi import print_exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd
import uuid
import json
import urllib.request

class Scraper:
    '''
    This class is a scraper that can be used to retrieve data from different websites

    Parameters:
    url: str
        The website URL for the site we want to scrape

    Attribute:
    driver:
        The webdriver object
    '''
    def __init__(self, url:str ='https://www.amazon.co.uk'):
        self.url = url
        #self.driver = Chrome(ChromeDriveManager().install())
        self.driver = Chrome('./chromedriver')
        self.driver.get(url)

    def accept_cookies(self, xpath: str = "//span[contains(@class,'on-primary')]"):
        '''
        This method looks for and clicks the accept cookies button

        Parameters:
        xpath: str
            The xpass of the cookies button
        '''
        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH, xpath).click()
        except:
            print('No cookies found')

    def search_site(self, xpath: str = "//input[contains(@id, 'search')]", query: str = 'Mobile Phones'):
        '''
        This method finds the search bar and enters a search query

        Parameters:
        xpath: str
            This is the xpath of the search bar
        query: str
            This is the query we want to search for
        '''
        time.sleep(1)
        searchbox = self.driver.find_element(By.XPATH, xpath)
        searchbox.send_keys(query)

    def click_go_button(self,xpath: str= "//input[@value='Go']"):
        '''
        This method searches for the 'go' button on the site

        Parameters:
        xpath: str
            This is the xpath of the 'go' button
        '''
        time.sleep(1)
        self.driver.find_element(By.XPATH, xpath).click()

    def find_links(self, xp_html: str= "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']"):
        '''
        This method finds all the links on the page and stores them in a list

        Parameters:
        xpath: str
        This is the xpath of the links on the page

        Returns:
        link_list: list
        This is a list of the urls on the page
        '''
        time.sleep(2)
        link_list = []
        container = self.driver.find_elements(By.XPATH, xp_html)
        for link in container:
            link_list.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        return link_list

    
    def create_dict(self, 
                    xp_title: str="//span[contains(@class, 'a-size-large product-title-word-break')]", 
                    xp_price: str="//span[contains(@class, 'a-price-whole')]",
                    xp_image: str= "//*[@id='landingImage']"):
        '''
        This creates a dictionary, and adds the name, price and unique identifier to each entry

        Parameters:
        xp_title: str
        This is the xpath of the product title on the page

        xp_price: str
        This is the xpath of the product price on the page

        Returns:
        dict_list: dictionary
        This is a dictionary containing url, title, price and unique identifier of each page
        '''
        link_list = self.find_links()
        dict_list = {
            'Link':[],
            'Name':[],
            'Price':[],
            'UUID':[],
            'image_url':[]
            }

        for link in link_list[0:4]:
            self.driver.get(link)
            time.sleep(2)
            dict_list['Link'].append(link)
            name = self.driver.find_element(By.XPATH, xp_title).text
            dict_list['Name'].append(name)
            price = self.driver.find_element(By.XPATH, xp_price).text
            dict_list['Price'].append(price)
            id = uuid.uuid4()
            dict_list['UUID'].append(id)
            image_url = self.driver.find_element(By.XPATH, xp_image).get_attribute('src')
            urllib.request.urlretrieve(image_url, f"{id}.jpg")

        
        print(pd.DataFrame(dict_list))
        print(dict_list)

        return dict_list
    
    def create_json(self):
        '''
        This method takes the dictionary and posts it as a json file

        Attribute:
        json.dumps:
            The object converts a python object into an equivalent JSON object
        '''
        dictionary = self.create_dict()
        file = json.dumps(dictionary)
        with open('file.json', 'w') as f:
            f.write(file)
            f.close()

    def close_driver(self):
        self.driver.quit()