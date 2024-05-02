import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\krshriva\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

dropdown =Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
time.sleep(5)
dropdown.select_by_index(0)
time.sleep(5)