# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 01:40:17 2020

@author: Hp
"""

DB = ['zohaib' , 100 , 3.142 , (1,2) , [20 , 30 , ('zak' , 100)]]

query = ['zohaib' , 100 , 3.142 , (1,2) , [20 , 30 , ('zak' , 100)] , "sample" , 999 , ('zzzz' ,8888)]


for search in query:
    if search in DB:
        print("{0} lies in the Database." . format(search))
    else:
        print("{0} DOESN'T lie in the Database." . format(search))