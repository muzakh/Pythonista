# -*- coding: utf-8 -*-
"""
1. Use returned output from a fn to somewhere else.
2. Assignment of data into two variables in the same line.
"""

var1 = input("Enter first numbers: ")
var2 = input("Enter first numbers: ")

def asc_order(var1, var2):
    if var1 > var2:
        return var1, var2
    else:
        return var2, var1
    

caught1, caught2 = asc_order(var1, var2)

print(caught1, "," , caught2)