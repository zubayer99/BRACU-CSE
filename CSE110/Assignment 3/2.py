# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:28:33 2022

@author: xyzub
"""

word=input()
lenword=len(word)
if lenword < 4:
    print(word)
elif lenword > 3 and word[-2:] == "er":
    new_word = word.replace("er", "est")
    print(new_word)
elif lenword > 3 and word[-3:] == "est":
    print(word)
elif lenword > 3:
    print(word + "er")
    
            

    