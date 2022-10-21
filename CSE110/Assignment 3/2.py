# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:28:33 2022

@author: xyzub
"""

word=input()
lenword=len(word)
if lenword < 4:
    print(word)
elif lenword > 3:
    print(word + "er")
if word.endswith("er"):
    print(word.replace("er", "est"))