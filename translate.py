#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:02:07 2020

@author: admin
"""

from googletrans import Translator
import requests
import json

def googletrans():
    translator = Translator()
    result = translator.translate("Jak się masz?", dest='pl')
    print(result.text)

def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    
    response = requests.post(url, data = data)
    json_data = json.loads(response.text)
    print(type(json_data))
    print(json_data['contents']['translated'])

piratetrans('I like eating apples')