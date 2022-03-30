import selenium

from selenium.webdriver import Chrome
driver = Chrome('./chromedriver')

url = 'https://www.amazon.co.uk/s?k=mobile+phones'
driver.get(url)

buttons = driver.find_element_by_xpath('//a[@type="button"]')

for button in buttons:
    if button.text == "Accept Cookies":
        relevant_button = button

    relevant_button.click()