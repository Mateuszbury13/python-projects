#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:10:12 2020

@author: admin
"""

from bs4 import BeautifulSoup
import urllib.request

url = input("url: ")
response = urllib.request.urlopen(url)

data = response.read()
doc = BeautifulSoup(data, 'parser')
list = doc.find_all('ol')
for li in list:
    i = 1
    list_items = li.find_all('li')
    print('\n')
    for lis in list_items:
        print(str(i) +'. ' + lis.get_text())
        i += 1



