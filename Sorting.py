import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browserSortedVeggis =[]
service_obj = Service("C:\\Users\\krshriva\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
VeeggieWebElement= driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in VeeggieWebElement:
    browserSortedVeggis.append(ele.text)

originalBrowserSortedList = browserSortedVeggis.copy()
browserSortedVeggis.sort()