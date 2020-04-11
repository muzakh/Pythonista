# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:47:32 2020

@author: Hp

Using Magic methods/Dunder Methods/Special methods to perform Addition operation b/w two class outputs
"""

class Sum(object):
    def __init__(self, a):
        self.a = a
        
    def __add__(self, b):
        return self.a + b.a



if __name__ == '__main__':
    x = Sum(5)
    y = Sum(10)
    print(x + y)
    type(x)
    type(y)
    type(Sum)
