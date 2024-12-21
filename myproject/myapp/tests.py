from django.test import TestCase

# automated testing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://127.0.0.1:8000/")

Player_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/a[1]")))
Player_button.click()

login_as_guest = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form/div[3]/a")))
login_as_guest.click()

book_now= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/button[1]")))
book_now.click()

Submit_drop_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/form/button")))
Submit_drop_box.click()

First_court_in_Cairo = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/ul/li[1]/a")))
First_court_in_Cairo.click()

view_schedule = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/form/button")))
view_schedule.click()

book_first_time_slot = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[3]/form/button")))
book_first_time_slot.click()

Notification_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[2]/a[3]")))
Notification_page.click()

#new line  

time.sleep(10)
driver.quit()

       
       


