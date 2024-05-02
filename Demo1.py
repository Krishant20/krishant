from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service("C:/Users/krshriva/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#driver= webdriver.chrome("C:/Users/krshriva/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.chrome()

driver.get("https://rahulshettyacademy.com/")
