# -*- coding: utf-8 -*-
"""
n! = n x (n-1)!
n! = n x (n-1) x (n-2)!
n! = n x (n-1) x (n-2) x ..... x 3 x 2 x 1

3! = 3 x 2 x 1
"""

'''
number = 0
val = 1
for var in range(1, (number + 1)):
    val = val * var

print(val)

'''
'''
===
OR
====
'''
''' 
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5)) 

'''

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print(fact(3))

