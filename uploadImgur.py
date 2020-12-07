#Made by Luca Santarella

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# add a delay so that all elements of
# the webpage are loaded before proceeding
import time
import os

# ChromeOptions allows us use the userdata of chrome
# so that you don't have to sign in manually everytime.
chropt = Options()

# adding userdata argument to ChromeOptions object (you could use it to skip the "accept cookie policy" part)
#chropt.add_argument("--user-data-dir=[insert-your-path-here]")

# Creating a Chrome webdriver object
driver = webdriver.Chrome(executable_path ="/bin/chromedriver",options = chropt)

#jump start to selected section
driver.get("https://imgur.com/upload")

#click agree on the cookie policy popup
elem_agree_button = driver.find_elements_by_class_name("sc-ifAKCX")
elem_agree_button[3].click()

driver.find_element_by_id("file-input").send_keys(os.getcwd()+"/pingu.jpeg")


time.sleep(15)

driver.close()
