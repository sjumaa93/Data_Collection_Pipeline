# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from sqlalchemy import create_engine

import time
import pandas as pd
import uuid
import json
import urllib.request
import sqlalchemy
import boto3
import os


class Scraper:
    def __init__(self, url: str = 'https://www.amazon.co.uk'):
        '''
        This class is a scraper that can be used to retrieve data from
        amazon, based on a search term

        The list of product URLs and the file data dictionary are initialized
        in this class

        The engine is also initialized in this class
        '''
        self.url = url
        options = Options()
        # options.add_argument('--headless')

        self.driver = Chrome(ChromeDriverManager().install(), options=options)
        # self.driver = Chrome('./chromedriver')
        self.driver.get(url)

        self.link_list = []
        self.product_data = {'Link': [], 'Name': [], 'Price': [], 'UUID': []}

        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'database.cqn1abbztdx3.us-east-1.rds.amazonaws.com'
        USER = 'postgres'
        PASSWORD = 'Blackberry12'
        DATABASE = 'postgres'
        PORT = 5432

        self.engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        self.client = boto3.client('s3')
        return

    def accept_cookies(self, xpath: str = "//span[contains(@class,'on-primary')]"):
        '''
        This method looks for and clicks the accept cookies button
        '''
        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH, xpath).click()
            print('Cookies Accepted ✅')
        except:
            print('No cookies found')
        return

    def search_site(self, xpath: str = "//input[contains(@id, 'search')]", query: str = 'Mobile Phones'):
        '''
        This method finds the search bar and enters a search query.
        '''
        time.sleep(1)
        searchbox = self.driver.find_element(By.XPATH, xpath)
        searchbox.send_keys(query)
        self.click_go_button()
        return

    def click_go_button(self, xpath: str = "//input[@value='Go']"):
        '''
        This method searches for the 'go' button on the site
        '''
        time.sleep(1)
        self.driver.find_element(By.XPATH, xpath).click()
        print('Searching site ⌛')
        return

    def find_links(self, xp_html: str = "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']"):
        '''
        This method finds all the links on the page and stores them in a list
        '''
        time.sleep(2)
        
        container = self.driver.find_elements(By.XPATH, xp_html)
        for link in container:
            self.link_list.append(link.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        return
    
    def create_dict(self,
                    xp_title: str = "//span[contains(@class, 'a-size-large product-title-word-break')]",
                    xp_price: str = "//span[contains(@class, 'a-price-whole')]",
                    xp_image: str = "//*[@id='landingImage']"):
        print('Collecting Product Data please wait... ⌛')
        '''
        This creates a dictionary, and adds the name, price and unique identifier to each entry

        This method also downloads the images and stores them in the images folder

        It then uploads the images to an s3 bucket
        '''
        for link in self.link_list[0:10]:
            self.driver.get(link)
            time.sleep(2)
            self.product_data['Link'].append(link)
            name = self.driver.find_element(By.XPATH, xp_title).text
            self.product_data['Name'].append(name)
            price = self.driver.find_element(By.XPATH, xp_price).text
            self.product_data['Price'].append(price)
            id = str(uuid.uuid4())
            self.product_data['UUID'].append(id)
            image_url = self.driver.find_element(By.XPATH, xp_image).get_attribute('src')
            urllib.request.urlretrieve(image_url, f"images/{id}.jpg")

            client = boto3.client('s3')
            client.upload_file(f'./images/{id}.jpg', 'myawsbucket9203', f'{id}')

        print('Product Scraped Successfully ✅')
        print('Images Uploaded successfully ⬆️')
        return

    def create_json(self):
        '''
        This method takes the dictionary and posts it as a json file
        '''
        with open("raw_data.json", "w") as f:
            json.dump(self.product_data, f)
        print('Saved as raw_data.json 💾')

        from botocore.config import Config

        my_config = Config(region_name='us-east-1')
        client = boto3.client('s3', config=my_config)

        client.upload_file('raw_data.json', 'myawsbucket9203', 'data.json')
        return

    def json_to_sql(self):
        '''
        This method takes json file and uploads it to the s3 server
        '''
        with open('./raw_data.json', 'r') as filename:
            data = json.load(filename)
            df = pd.DataFrame(data)
            df.columns = df.columns.str.lower()
            self.engine.connect()
            df.to_sql('raw_data', con=self.engine, if_exists='replace')
            print('uploaded to SQL database ⬆️')
        return

    def remove_local_images(self):
        '''
        This method removes local images in the directory '/images'
        '''
        dir = './images/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        return

    def close_driver(self):
        '''
        This method closes the driver
        '''
        self.driver.quit()
        return
