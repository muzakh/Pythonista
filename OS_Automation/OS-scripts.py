# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 02:17:23 2020

@author: Hp
"""

import os
import sys
import glob
from PIL import Image
#import gfx
import pickle


path = os.path.join("F:/")
print("\n Current Directory: {0}" . format(os.getcwd()))
print("\n Changing directory to {0}" . format(path))
os.chdir(path)
print("\n Changed path is {0}" . format(os.getcwd()))
print("\n List Dir contents: {0}" . format(os.listdir(os.curdir)))

print("\n Environment Variables of system are {0}\n" . format(os.environ.items()))


''' Displaying environment variables in cleaner way '''
for var in os.environ.keys():
    print(var, os.environ[var])
    
''' Displaying current directory contents in cleaner way '''
for var in os.listdir(os.curdir):
    print(var)
    
''' Printing name like nt or POSIX'''
print(os.name)

''' Printing sys platform/more details like win32 or linux2'''
print(sys.platform)

''' Renaming and then Removing a file/folder  '''
os.chdir("E:/E/latest Stuff/Python Programing/CBT Nuggets - Python Programming Python Language/My Revisions/third revision")
print("Listing Directory contens: \n {0}" . format(os.listdir()))
os.mkdir("workspace")
os.rename("workspace" , "Dir-Ranamed-via-Python-OS-Module")
print("Listing Dir contents after rename: \n {0}" . format(os.listdir()))

print("Now removing directory\n")
os.rmdir("Dir-Ranamed-via-Python-OS-Module")
''' 
os.rmdir() --> removes a directory
os.remove() --> removes a file
'''

''' ### Playing with Files ### '''
alist = ['Zohaib', 'Asim', 'Khan']
path2 = os.path.join(os.getcwd(), "files", "")

os.remove("{0}file1.txt" . format(path2))

f = open("{0}file1.txt" . format(path2), 'w')
f.write("This is the first line.\n")
f.write("This is the second line.\n")
f.writelines(alist)
f.close()

f = open("{0}/file1.txt" . format(path2), "r")
f.readline()
f.close()


''' ###  Read contens from a file  ###  '''  
f = open("{0}file1.txt" . format(path2) , 'r')
f.seek(0)

''' Counting Total lines in a file ''' 
LinesCount = len(f.readlines())

for line in f.readlines():
    print(line, end="")
    print(len())

''' Printing total number of lines '''
print("\nTotal lines are: {0} \n" . format(LinesCount))
f.close()


''' 
### LIST ALL DIRECTORIES RECURSIVELY ALONG WITH TOTAL COUNT OF FILES  #### 
'''
print("\n\n *** All Recursive Directories with their counts *** \n")
for parent_dir, subdir_list, files_list in os.walk(os.curdir):
    Total_file_folder_Count = len(subdir_list) + len(files_list)
    print(parent_dir, subdir_list, files_list, "\n Files Count : {0} and Total(Files + Folder) Count : {1} \n" . format(len(files_list), Total_file_folder_Count))
        

''' ### Working with GLOB for WildCard searching  ###  ''' 
print("\n\n ### Searching through GLOB ###")
''' Here we are searching .py files on using wildcard *.py using glob() method  '''
for var in glob.glob(os.path.join(os.getcwd(), "*.py")):
    print(var)


''' 
### Read Image and PDF files using Image and gfx modules  #### 
'''
f = Image.open(os.path.join(os.getcwd(), "zohaib.jpg"))
f.show()
f.close()

'''
f = gfx.open(os.path.join(os.getcwd(), "zohaib.pdf"))
print(type(f))
f.close()
'''


''' 
### Making data structure portable using pickle module  #### 
'''
'''
adataSt = ['zohaib', 27, 1989, 3.18, ['NED', 'KU'], (2018, 2011, ['B', 'A'])]

f = open(os.path.join(os.getcwd(), "files", "pickle_file.txt"), "wb")

pickle.dump(adataSt, f)

f.close()

f = open(os.path.join(os.getcwd(), "files", "pickle_file.txt"), 'r')

adataSt_new = pickle.load(f)

f.close()
'''


