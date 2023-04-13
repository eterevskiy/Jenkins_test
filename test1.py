from selenium import webdriver
import os 
import time
driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver'))
try :
    driver.get('https://www.google.com/')
    time.sleep(3)
    driver.get_screenshot_as_file('result.png')
except Exception as err:
    print(err)