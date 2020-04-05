# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 01:49:01 2020

@author: Hp
"""

def addfn(x,y):
    sumv = x + y
    print("Sum of {0} and {1} is : {2}" . format(x, y, sumv))
    return

def subtfn(x,y):
    subtv = x - y
    print("Difference of {0} and {1} is : {2}" . format(x, y, subtv))
    return

def quitf():
    raise SystemExit("Exiting from the program.")


print("""
   1.  Adding. Press (a)
   2.  Adding. Press (s)
   
""")

while True:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    inp = input("Enter string or 'Q' to quit: ").lower()
    
    
    if (inp[0] == "q" and len(inp) == 1) or inp == "quit":
        quitf()
        
    elif inp[0] == "a":
        addfn(num1, num2)
        
    elif inp[0] == "b":
        subtfn(num1, num2)
        
    else:
        print("Please select valid options from the list provided.")
        continue