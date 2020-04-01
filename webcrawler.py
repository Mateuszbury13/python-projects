#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:51:07 2020

@author: admin
"""

import urllib.request
from bs4 import BeautifulSoup

print('Getting staff urls...')

staff_url = 'http://wa.amu.edu.pl/wa/pl/staff_list'
response = urllib.request.urlopen(staff_url)
data = response.read()
doc = BeautifulSoup(data, 'html.parser')

staff_content = doc.find(id='tresc_wlasciwa')

links = staff_content.find_all('a')

print(links)