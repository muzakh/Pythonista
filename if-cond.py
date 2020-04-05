# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:01:20 2020

@author: Zohaib
program : fetch elements from the list
"""

alist = ['Programmer', 'SysAdmin', 'Teacher']

inp = input(""" Enter characters are follows:
    'P' for Programmer
    'S' for SysAdmin
    'T' for teacherp
""")
    
conv_input = inp.lower()


if conv_input[0] == "p" and len(conv_input) == 1:
    print("User selected for : {0}" . format(alist[0]))

elif conv_input[0] == "s" and len(conv_input) == 1:
    print("User selected for : {0}" . format(alist[1]))
    
elif conv_input[0] == "t" and len(conv_input) == 1:
    print("User selected for : {0}" . format(alist[2]))
    
else:
    print("Invalid output '{0}', Exiting now!" . format(conv_input))
