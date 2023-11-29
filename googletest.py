from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
import os

chrome_driver_path = 'C:\\Program Files (x86)\\Google\\chromedriver.exe'
url = 'https://www.google.com'


driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get(url)

element = driver.find_element(By.NAME, "q")
element.send_keys('wolverine')
element.submit()
time.sleep(5)

home_directory = os.path.expanduser("~")

relative_path = os.path.join("Pictures", "py", "wolverine.png")

capture_path = os.path.join(home_directory, relative_path)

driver.save_screenshot(capture_path)

element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys('Jupiter')
element.submit()
time.sleep(5)
home_directory = os.path.expanduser("~")

relative_path = os.path.join("Pictures", "py", "Jupiter.png")

capture_path = os.path.join(home_directory, relative_path)

driver.save_screenshot(capture_path)

driver.quit()




