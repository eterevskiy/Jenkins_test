from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os 
import time
chrome_path = '/usr/bin/google-chrome'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
service = Service(executable_path=os.path.join(os.getcwd(),'chromedriver'))
driver = webdriver.Chrome(service=service, options=chrome_options,executable_path=chrome_path)
try :
    driver.get('https://www.google.com/')
    time.sleep(3)
    driver.get_screenshot_as_file('result.png')
except Exception as err:
    print(err)