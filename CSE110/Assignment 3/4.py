# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 20:02:45 2022

@author: xyzub
"""

string=input()
for i in range(0,len(string)):
      x=ord(string[i])
      if chr(x+1) > 122:
          
      print(chr(x+1))
    