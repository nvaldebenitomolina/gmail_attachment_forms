
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import re
import operator
import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import datetime
import shutil

fecha=str(datetime.datetime.now()).split(' ')[0]
print(fecha)

#open webdriver
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
print('user: cr2dgf password:wpcr2')
driver.get("http://www.cr2.cl/wp-admin/")

user=os.environ["USER_WORDPRESS"]
password=os.environ["PASSWORD_WORDPRESS"]

time.sleep(8)
#username
username = driver.find_element_by_xpath('//*[@id="user_login"]')
username.send_keys(user)

#password
userpassword = driver.find_element_by_xpath('//*[@id="user_pass"]')
userpassword.send_keys(password)

button = driver.find_element_by_xpath('//*[@id="wp-submit"]')
button.click()
driver.maximize_window()
time.sleep(4)
driver.get("http://www.cr2.cl/wp-admin/admin.php?page=flamingo_inbound&s&_wpnonce=6ebff0d6ab&_wp_http_referer=%2Fwp-admin%2Fadmin.php%3Fpage%3Dflamingo_inbound&action=-1&m=0&channel_id=1558&paged=1&action2=-1")

driver.find_element_by_xpath('//*[@id="export"]').click()
time.sleep(5)
cwd = os.getcwd()
file='centrodecienciadelclimaylaresiliencia-cr2-flamingo-inbound-'+fecha
shutil.move("/home/nvaldebenito/Descargas/"+file+'.csv', cwd+"/"+file+'.xlsx')
