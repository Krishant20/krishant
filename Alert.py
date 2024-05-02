import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\krshriva\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
name = "Krishan"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Krishant")
#driver.find_element(By.XPATH,"//input[@value='Confirm']").click()
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert.Text = alert.text
print(alert.Text)
assert name in alert.Text
alert.accept()
#alert.dismiss()
