# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:31:52 2020

@author: Zohaib

Description: 
Using Decorator func to perform division by selecting larger number as numerator of given two numbers.

"""

''' Achieving without a decorator fuction
def div(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    return num1/num2
'''

def decorator_smart_div(fn):
    ''' Inner function/wrapped fn is the actual fun inside the decorator that does actual job '''
    def inner(num1,num2):
        if num1 < num2:
            num1, num2 = num2, num1
        return fn(num1, num2)
    return inner


@decorator_smart_div
def div(num1, num2):
    return num1/num2


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print(div(num1, num2))
