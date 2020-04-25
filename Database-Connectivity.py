# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:15:29 2020

@author: Zohaib

Description : Connection With Database using SQLite DB API. 

Program to create a table and fetch its records from the Database.

"""

import os, sqlite3


DataBase="Employees_DB"

os.chdir("E:\wirecard")
os.remove(DataBase)

con = sqlite3.connect(DataBase)
cur = con.cursor()

cur.execute(""" CREATE TABLE EMPLOYEES (ID integer primary key, NAME varchar2(20) , OCCUPATION varchar2(20)) """)
cur.execute(""" insert into employees values(1, 'Zohaib', 'Lead DevOps Engineer') """)
cur.execute(""" insert into employees values(2, 'Tim', 'SRE Engineer') """)
cur.execute(""" INSERT INTO EMPLOYEES VALUES(3, 'Anthony', 'Network Engineer') """)

con.commit()
cur.execute(""" SELECT * FROM EMPLOYEES """)

print(cur.fetchall())
con.close()

