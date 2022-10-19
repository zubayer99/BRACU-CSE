# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 23:01:56 2022

@author: xyzub
"""

x=0
counter=0
for i in range(0,601):
    if i % 7 == 0 and i % 9 == 0:
        counter+=i
        if i % 7 == 0 or i % 9 == 0:
            