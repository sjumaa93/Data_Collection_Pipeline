import selenium
from selenium.webdriver import Chrome
driver = Chrome('./chromedriver')
driver.maximize_window()

driver.get('https://www.amazon.co.uk/')
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[contains(@id,'search')]").send_keys("mobile phone")
#driver.find_element_by_xpath("//span[contains(@class, 'a-size-medium a-color-base a-text-normal'")

phone_names = driver.find_element_by_class_name("a-size-medium a-color-base a-text-normal")
phone_price = driver.find_element_by_class_name("a-price-whole")

for phone in phone_names:
    print(phone.text)

for price in phone_price:
    print(price.text)