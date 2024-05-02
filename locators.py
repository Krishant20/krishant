import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\krshriva\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Deva")
driver.find_element(By.NAME,"email").send_keys("Krishant")
time.sleep(2)
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Krishant@1")
time.sleep(2)
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[value='option1']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
Message =driver.find_element(By.CLASS_NAME,"alert-success").text
print(Message)
assert "Success" in Message

#driver.find_element(By.XPATH,"//input[@type='text'][3]").send_keys("Deva")

