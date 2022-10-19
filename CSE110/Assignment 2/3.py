# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:54:31 2022

@author: xyzub
"""

counter=0
for i in range(0,601):
    if i % 7 == 0 and i % 9 == 0:
        counter=counter+i
print(counter)