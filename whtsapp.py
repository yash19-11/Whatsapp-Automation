from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

target = '"We dont suckk"'

string = "Message sent using Python!!!"

x_arg = '//span[contains(@title,' + target + ')]'

group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))

group_title.click()

inp_xpath = "//div[@title ='Type a message']"

input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

input_box.send_keys(string)
input_box.send_keys(Keys.ENTER)
time.sleep(1)