# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 20:02:45 2022

@author: xyzub
"""

u_input=input()

for i in u_input:
    ascii_val = ord(i)
    ascii_val +=1
    
    if ascii_val > 122:
        ascii_val = 97
    
    ch = chr(ascii_val)
    print(ch, end = "")
    