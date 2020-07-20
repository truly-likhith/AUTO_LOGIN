#AUTO LOGIN PROJECT
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time 
driver=webdriver.Chrome()
driver.get('http://facebook.com')

emailelement=driver.find_element(By.XPATH,'.//*[@id="email"]')
un=input("Enter Email id:")
emailelement.send_keys(un)
passelement=driver.find_element(By.XPATH,'.//*[@id="pass"]')
up=input("Enter password:")
passelement.send_keys(up)

elem=driver.find_element(By.XPATH,'.//*[@id="loginbutton"]')
elem.click()
statuselement=driver.find_element(By.XPATH,".//*[@name='xhpc_message']")
statuselement.send_keys('Hi there')
time.sleep(5)
buttons=driver.find_element_by_tag_name('button')
time.sleep(5)
for button in buttons:
    if button.text=='Post':
        button.click()	