from sys import implementation
from typing import final


from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Scraper:
    def __init__ (self,url, options):
        self.url = url
        self.driver = Chrome(driver = Chrome('./chromedriver'), options=options)


    def accept_cookies(self, xpath):
        cookies_button = self.driver.find_element(By.XPATH, xpath)
        cookies_button.click()


driver = Chrome('./chromedriver')

url = 'https://www.amazon.co.uk/'
driver.get(url)

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[contains(@class,'on-primary')]").click()
driver.find_element(By.XPATH,"//input[contains(@id, 'search')]").send_keys("Mobile Phones")
driver.find_element(By.XPATH,"//input[@value='Go']").click()

phone_name = driver.find_elements(By.XPATH,"//span[contains(@class, 'a-size-medium a-color-base a-text-normal')]")
phone_price = driver.find_elements(By.XPATH,"//span[contains(@class, 'a-price-whole')]")

myphone=[]
myprice=[]

for phone in phone_name:
    myphone.append(phone.text)

print("*"*50)

for price in phone_price:
    myprice.append(price.text)

final_list = zip(myphone,myprice)

for data in list(final_list):
    print(data)