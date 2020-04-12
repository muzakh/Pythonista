# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:54:20 2020

@author: Zohaib
Usage of generators to free up memory. Print perfect squares of given range of numbers
"""



def perfect_square(num):
    ''' We can also use while loop here while i <= num: yield i**2 '''
    for i in range(1, num + 1):
        yield i **2
    

if __name__ == '__main__':
    
    num = int(input("Enter range: "))
    gen = perfect_square(num)
    
    type(gen)
    
    for var in gen:
        print(var)
