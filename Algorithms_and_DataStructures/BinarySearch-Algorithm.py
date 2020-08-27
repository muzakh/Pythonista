'''
Program: Binary Searching Algorithm (List must be pre-sorted for binary search)
List [2, 4, 10, 14, 17, 22]

Task : search 'n' in given list of Numbers and also prints it index value

'''

index = -1 # Just for debugging 

def search(alist, n):
    lowerBound = 0
    upperBound = len(alist) -1
    
    while (lowerBound <= upperBound):
        midvalue = (lowerBound + upperBound) // 2
        
        if n == alist[midvalue]:
            globals()['index'] = midvalue # Changing value of global variable inside a function locally
            return True
            
        else:
            if n < alist[midvalue]:
                upperBound = midvalue - 1
            
            elif n > alist[midvalue]:
                lowerBound = midvalue + 1
                
    return False


alist = [2, 4, 10, 14, 17, 22]
n = 14
#n = 99
if search(alist, n):
    print("{0} found at index: {1}" .format(n, index))
    
else:
    print("{0} NOT found" . format(n))








