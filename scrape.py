import os
import sys
from collections import defaultdict
import datetime
import pickle
import re
import time
import json
from selenium import webdriver

def main():
    driver = webdriver.Chrome() # Optional argument, if not specified will search path.
    #load login cookie
    driver.get('https://www.messenger.com')
    cookies=pickle.load(open('data/logincookies.pkl','rb'))
    for c in cookies:
        driver.add_cookie(c)
    driver.get('https://www.messenger.com')
    #get page source
    source=(driver.page_source).encode('utf8','replace')

    #get  last active times and add them to database
    v=re.compile("lastActiveTimes\":(.*),\"chatNotif")
    lolo=json.loads(v.findall(source)[0])
    d=defaultdict(lambda:[0],json.load(open("data/lastActiveTimes.json",'r')))
    for k in lolo:
        if lolo[k]!=d[k][-1]:
            d[k].append(lolo[k])
    json.dump(d,open("data/lastActiveTimes.json",'w'))

    #maintain up to date database of friends profiles
    v=re.compile("shortProfiles\":(.*),\"nearby")
    lala=json.loads(v.findall(source)[0])
    d=json.load(open('data/shortProfiles.json','r'))
    d.update(lala)
    json.dump(d,open('data/shortProfiles.json','w'))
    driver.quit()

if not os.path.exists('data/logincookies.pkl'):
    print ('missing cookie. Have you run init.py?')
    sys.exit()


while True:
    main()
    with open('data/lastScrapeTime.txt','a') as f:
        f.write(str(datetime.datetime.now())+'\n')
    time.sleep(600)
