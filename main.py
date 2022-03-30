from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import Chrome
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
    print(phone.text)
    myphone.append(phone.text)

print("*"*50)

for price in phone_price:
    print(price.text)
    myprice.append(price.text)

final_list = zip(myphone,myprice)

for data in list(final_list):
    print(data)