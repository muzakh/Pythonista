# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:34:08 2020

@author: Zohaib

"""

while True:
    inp = input("Enter string of atleast 4 characters and press Q/Quit to exit: ").lower()

    if (inp[0] == "q" and len(inp) == 1) or inp == "quit":
        raise SystemExit(3)
        #break
    
    else:
        
        if len(inp) < 4:
            print("Input value too small. Please provide it again!")
            continue
        
        else:
            print("User provided : {0} with length:{1}" . format(inp, len(inp)))