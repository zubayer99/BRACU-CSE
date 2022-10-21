# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:28:33 2022

@author: xyzub
"""

word=input()
for i in range(len(word)+1):
    if len(word) < 4:
        print(word)
    elif len(word) > 3:
        print(word + "er")
    elif len(word)