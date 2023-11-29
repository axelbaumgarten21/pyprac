from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

chrome_driver_path = 'C:\\Program Files (x86)\\Google\\chromedriver.exe'
url = 'https://www.google.com'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the specified URL in the browser
driver.get(url)

element = driver.find_element(By.NAME, "q")
element.send_keys('wolverine')
element.submit()
time.sleep(5)
capture_path = 'C:/Users/Ax/Pictures/py/wolverine.png'
driver.save_screenshot(capture_path)

element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys('Jupiter')
element.submit()
time.sleep(5)
capture_path = 'C:/Users/Ax/Pictures/py/Jupiter.png'
driver.save_screenshot(capture_path)

driver.quit()





