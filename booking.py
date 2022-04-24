import time 
import pause, datetime
 
#from datetime import datetime
from tkinter import E
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

'''
ist=time.localtime()
a = time.strftime("%H:%M:%S", ist)
x = int(round(time.time() * 1000))
print(a,x)
'''

s=Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s)
try:
    driver.get("https://gess.ultimatix.net/gess/pages/GESS/Travel/Home/HolidayHomesInitationHome.jsf")
    driver.implicitly_wait(2)
    text_area = driver.find_element_by_id("form1")
    text_area.send_keys("1862316")
    element = driver.find_element_by_xpath("//*[@id='proceed-button']").click()
    element = driver.find_element_by_xpath("//*[@id='easyAuth-btn']").click()
    
except Exception as e:
    print(e)
driver.implicitly_wait(5)

element = driver.find_element_by_xpath("//*[@id='holidayHomesInitForm:_idJsp155:2:_idJsp156']").click()
element = driver.find_element_by_xpath("//*[@id='holidayHomesInitForm:roomType']/option[3]").click()
element = driver.find_element_by_xpath("//*[@id='holidayHomesInitForm:termsConditions']").click()

element = driver.find_element_by_xpath("//*[@id='holidayHomesInitForm:row1:3:col1:1_1:date1']").click()
element = driver.find_element_by_xpath("//*[@id='holidayHomesInitForm:row1:3:col1:3_3:date1']").click()
#dt = datetime.datetime(2022, 4, 24, 7, 57, 00, 000000)
#print("Before clicking",datetime.datetime.now())
#driver.implicitly_wait(5)
dt = datetime.datetime(2022, 4, 24, 8, 00, 00, 000000)

pause.until(dt)

element = driver.find_element_by_xpath("//*[@id='holidayHomesInitForm:book1']").click()
print("After clicking",datetime.datetime.now())
#print(driver.title)
#driver.implicitly_wait(20)
#driver.close()

'''
ist=time.localtime()
a = time.strftime("%H:%M:%S", ist)
x = int(round(time.time() * 1000))
print(a,x)
'''