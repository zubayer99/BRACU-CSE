# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:59:39 2022

@author: xyzub
"""

counter=0
for i in range(0,601):
    if i % 7 == 0 or i % 9 == 0:
        counter+=i
print(counter)