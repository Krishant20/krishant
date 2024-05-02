import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\krshriva\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products'] /div")
count = len(results)

assert count > 0

for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH,"//input[@class='promoCode' and @placeholder ='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
Value =driver.find_element(By.CSS_SELECTOR,".promoInfo")
print(Value.text)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()