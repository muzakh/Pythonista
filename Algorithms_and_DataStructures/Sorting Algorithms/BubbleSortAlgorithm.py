'''
Bubble Sort Algorithm:

Sorting in Ascending Order

[5, 3, 8, 6, 7, 2]

Note: In every Iteration elements with larger values are swapped at the right most side. In every iteration we are moving right to left.

https://www.youtube.com/watch?v=Vca808JTbI8

'''


def bubble_sort(alist):
    
    for trav in range(len(alist) -1, 0, -1):  # You can decide any direction to enumerate. Here we are moving from left to right in the list. So the outermost loop will be enumerated from right to left
        for j in range(trav):
            
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp


alist = [5, 3, 8, 6, 7, 2]

bubble_sort(alist)

print(alist)

'''
Result
======
[2, 3, 5, 6, 7, 8]
'''

'''
OR
===

Use Python Built-in Sort function:
==================================

alist = [5, 3, 8, 6, 7, 2]

alist.sort()

print(alist)


[2, 3, 5, 6, 7, 8]



FOr descending order:
=====================

alist.sort(reverse = True)



alist = [5, 3, 8, 6, 7, 2]

alist.sort(reverse = True)

print(alist)



[8, 7, 6, 5, 3, 2]

'''


'''
************************************
Optimized Code showing all the iterations
************************************
'''

def Bubble_sort(alist):
    
    count = 0
    for i in range(len(alist) -1, 0, -1):
        
        count = count + 1 
        print("\nInteration # {}:" . format(count))
        
        for j in range(0, i):
            
            if alist[j] > alist[j + 1]:
                
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
            
            print("Bubble Sorting: {}" . format(alist))



alist = [5, 3, 8, 6, 7, 2]

Bubble_sort(alist)

print("\nFinal Sorted List is {0}" . format(alist))


'''
Interation # 1:
Bubble Sorting: [3, 5, 8, 6, 7, 2]
Bubble Sorting: [3, 5, 8, 6, 7, 2]
Bubble Sorting: [3, 5, 6, 8, 7, 2]
Bubble Sorting: [3, 5, 6, 7, 8, 2]
Bubble Sorting: [3, 5, 6, 7, 2, 8]

Interation # 2:
Bubble Sorting: [3, 5, 6, 7, 2, 8]
Bubble Sorting: [3, 5, 6, 7, 2, 8]
Bubble Sorting: [3, 5, 6, 7, 2, 8]
Bubble Sorting: [3, 5, 6, 2, 7, 8]

Interation # 3:
Bubble Sorting: [3, 5, 6, 2, 7, 8]
Bubble Sorting: [3, 5, 6, 2, 7, 8]
Bubble Sorting: [3, 5, 2, 6, 7, 8]

Interation # 4:
Bubble Sorting: [3, 5, 2, 6, 7, 8]
Bubble Sorting: [3, 2, 5, 6, 7, 8]

Interation # 5:
Bubble Sorting: [2, 3, 5, 6, 7, 8]

Final Sorted List is [2, 3, 5, 6, 7, 8]

'''
