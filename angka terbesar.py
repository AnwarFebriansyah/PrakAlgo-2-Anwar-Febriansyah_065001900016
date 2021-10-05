# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:12:56 2021

@author: HP
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

maks = 0
if a > b:
    maks = a
else:
    maks = b
    
if c > maks:
    maks = c
    
print(" Angka Terbesar: ",maks)
       
       