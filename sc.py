from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from webdriver.manager
import time

driver =  webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.com')
time.sleep(10)
driver.quit()