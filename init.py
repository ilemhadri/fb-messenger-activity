import time
import json
import os
import getpass
import pickle
from selenium import webdriver

if not os.path.exists('data'):
    os.makedirs('data')

#initialize empty database for last active times
lastActiveTimes={}
json.dump(lastActiveTimes,open('data/lastActiveTimes.json','w'))
#initialize empty database for user profiles
shortProfiles={}
json.dump(shortProfiles,open('data/shortProfiles.json','w'))
#login to Messenger using your credentials
#replace MYEMAIL by your Facebook email and MYPASSWORD by your Facebook password
myemail=raw_input('Enter your email: ')
print('using email %s'%myemail)
mypassword=getpass.getpass(prompt= myemail+'\'s password: ')
print('logging in to Messenger')
time.sleep(1)
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.messenger.com')
time.sleep(1)
(driver.find_element_by_id("email")).send_keys(myemail)
(driver.find_element_by_id("pass")).send_keys(mypassword)
(driver.find_element_by_id("loginbutton")).click()
#save the login credentials into a cookie for later use
pickle.dump(driver.get_cookies(), open('data/logincookies.pkl','wb'))
driver.quit()