# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:26:04 2020

@author: Hp
"""


astring = input("enter string value:")
ainteger = int(input("enter integer:"))
afloat = float(input("enter float:"))

alist = ["zohaib", 1, 3.142]
atup = ('anas', 71, 33.5)
adict = {1:"apple", 2:100, 3:100.99}

print("List is : ", alist)
print("Tuple is :", atup)
print("Dictionary is :", adict)

print("\n" * 2)

alist.append(astring)

print("New List : " ,alist)
print("New Tuple : ", atup)
print("New Dictionary : ", adict)

print('\n' * 2)
print("Type of List : ", type(alist))
print("Type of Tuple : ", type(atup))
print("Type of Dictionary : ", type(adict))

