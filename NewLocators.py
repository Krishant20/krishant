import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\krshriva\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT,'Forgot password?').click()
time.sleep(2)