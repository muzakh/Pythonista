# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 07:29:21 2020

@author: Zohaib
Name : table.py
Purpose : To print the multiplier tables of given range of numbers up till 10.
"""

first_num = int(input("Enter starting number: "))
second_num = int(input("Enter ending number: "))

print('''
   ***  M U L T I P L I E R   T A B L E  ***   
''')

print("\n")

for table_number in range(first_num, (second_num + 1)):
    print("Table of Number : {0}" . format(table_number))
    
    for multiples in range(1,11):
        print("{0} x {1} = {2}" . format(table_number, multiples, (table_number * multiples)))

