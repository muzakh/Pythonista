'''
Bubble Sort Algorithm:

Sorting in Ascending Order

[5, 3, 8, 6, 7, 2]

Note: In every Iteration elements with larger values are swapped at the right most side. In every iteration we are moving right to left.

https://www.youtube.com/watch?v=Vca808JTbI8

'''


def bubble_sort(alist):
    
    for trav in range(len(alist) -1, 0, -1):  # You can decide any direction to enumerate. Here we are moving from left to right in the list.
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


