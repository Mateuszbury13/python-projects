#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:02:07 2020

@author: admin
"""

from googletrans import Translator

def main():
    translator = Translator()
    result = translator.translate("Jak się masz?", dest='de')
    print(result.text)

main()