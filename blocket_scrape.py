# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
import urllib.request
import requests
import csv
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for i in range(20):
    http = urllib3.PoolManager()
    url = "https://www.blocket.se/bostad/saljes/stockholm?ac=0MNXXY7CTORXWG23IN5WG2000&o={}".format(i)
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html5lib")
    
    for i,j in zip(soup.find_all('span', attrs={'class':'li_detail_params size'}), 
               soup.find_all('span', attrs={'class':'li_detail_params first price'})):
        print (i.text.replace("mÂ²", ""), ",", j.text.replace("kr", "").replace(" ", ""))