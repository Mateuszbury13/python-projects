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



