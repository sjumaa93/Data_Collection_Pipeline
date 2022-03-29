import csv
from re import template
import selenium
from bs4 import BeautifulSoup

from selenium.webdriver import Chrome
driver = Chrome('./chromedriver')

url = 'https://www.amazon.co.uk/s?k=mobile+phones'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.fin_all('div', {'date_'})