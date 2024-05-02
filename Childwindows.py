import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\krshriva\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowhandle = driver.window_handles

driver.switch_to.window(windowhandle[1])
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.switch_to.window(windowhandle[0])
print(driver.find_element(By.CSS_SELECTOR,"h3").text)

assert "Opening a new window" ==  driver.find_element(By.CSS_SELECTOR,"h3").text