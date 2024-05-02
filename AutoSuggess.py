import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\krshriva\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
Countries = driver.find_elements(By.XPATH, "//li[@Class='ui-menu-item']/a")
print(len(Countries))


for country in Countries:
    if country.text == "India":
        country.click()
        break
