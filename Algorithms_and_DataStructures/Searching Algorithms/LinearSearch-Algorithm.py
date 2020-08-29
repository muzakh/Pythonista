'''
Program: Linear Searching Algorithm
List [10, 9, 8, 4, 1, 50]

Task : search 'n' in given list of Numbers and also prints it index value
E.g: Input would be a List and a Number

'''
index=-1

def search(alist, n):
    
    i = 0
    while (i < len(alist)):
        if alist[i] == n:
            globals()['index'] = i
            return True
            
        i = i + 1
            
    return False


alist = [10, 9, 8, 4, 1, 50]
#n = 4
n = 30

if search (alist, n):
    print("Found at {0}" . format(index))
    
else:
    print("Not Found")


'''
Result
$python3 main.py
Not Found
'''


'''
Ssme Peice of code using For loop
'''

index=-1

def search(alist, n):
    
#    i = 0
    for i in range (len(alist)):
        if alist[i] == n:
            globals()['index'] = i
            return True
            
    #    i = i + 1
            
    return False


alist = [10, 9, 8, 4, 1, 50]
#n = 1
n = 100

if search (alist, n):
    print("Found at {0}" . format(index))
    
else:
    print("Not Found")
