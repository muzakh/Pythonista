'''
Program: Selection Sort Algorithm
Description: Bubble Sort consumes more processing power (CPU and Memory) than Selection Sort because Section Sort swap values in outer loop i.e at once in every iteration whereas Bubble sort, on the other hand, swaps values in the inner loop i.e multiple times in every iteration.

It iterates over the loop and tracks min values and then only performs the swapping 

[5, 3, 8, 6, 7, 2]

'''

def selection_sort(alist):
    for trav in range(len(alist) - 1): # -1 is used because there is no need to check and iterate over the last element of the sorted list as it will already be the largest number of all remaining at the end.
        min_value = trav
        
        for j in range(trav, len(alist)):
            if alist[j] < alist[min_value]:
                
                min_value = j
                
        temp = alist[trav]
        alist[trav] = alist[min_value]
        alist[min_value] = temp
        
        print("Selection Sort Iteration : {}" .format(alist))



alist = [5, 3, 8, 6, 7, 2]
selection_sort(alist)

print("\n Final Sorted List: {}" . format(alist))



'''
Result
======
Selection Sort Iteration: [2, 3, 8, 6, 7, 5]
Selection Sort Iteration: [2, 3, 8, 6, 7, 5]
Selection Sort Iteration: [2, 3, 5, 6, 7, 8]
Selection Sort Iteration: [2, 3, 5, 6, 7, 8]
Selection Sort Iteration: [2, 3, 5, 6, 7, 8]

 Final Soted List [2, 3, 5, 6, 7, 8]:

'''

