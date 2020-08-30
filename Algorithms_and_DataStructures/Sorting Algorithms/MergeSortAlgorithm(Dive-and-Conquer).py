
'''
Merge Sort Algorithm (Divide and Conquer Algorithm): 
====================================================

Uses recursice function calls

Complexity:
==========
Complexity is O(n logn)
Steps of Merge Sort = base 2 log of N where N is the total of elements in the list. For instance, a list of 8 elements would have 3 steps for merge sort.
log2 (8) = 2^3

And for every Merge Step it does n work so complexity becomes (n * log n)

Links:
https://www.youtube.com/watch?v=Nso25TkBsYI&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=4

https://www.youtube.com/watch?v=jlHkDBEumP0


Unsorted Given List: [17, 87, 6, 22, 41, 3, 13, 54]
'''


#Unsorted Given List: [17, 87, 6, 22, 41, 3, 13, 54]

def Merge_Sort(alist):
    sorting_list(alist, 0, len(alist) -1)
    
def sorting_list(alist, first, last):
    if first < last:
        mid_index = (first + last) // 2
        sorting_list(alist, first, mid_index)
        sorting_list(alist, mid_index + 1, last)
        merge_list(alist, first, mid_index, last)

def merge_list(alist, first, mid_index, last):
    L = alist[:mid_index]
    R = alist[mid_index:]
    
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            alist[k] = L[i]
            i = i + 1
        else:
            alist[k] = R[j]
            j = j + 1
            
        k = k + 1
        
    while i < len(L):
        alist[k] = L[i]
        i = i + 1 
        k = k + 1
        
    while j < len(R):
        alist[k] = R[j]
        j = j + 1
        k = k + 1


alist = [17, 87, 6, 22, 41, 3, 13, 54]
#alist = [15, 5, 24, 8, 1, 3, 16, 10, 20]

Merge_Sort(alist)

print("Final Merged Sorted List: {}" . format(alist))

'''
Result:
========
Final Merged Sorted List: [3, 6, 13, 17, 22, 41, 54, 87]
'''

'''
OR
https://www.geeksforgeeks.org/merge-sort/
'''

# Python program for implementation of MergeSort 
def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 # Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1

# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i], end =" ") 
	print() 

# driver code to test the above code 
if __name__ == '__main__': 
	arr = [17, 87, 6, 22, 41, 3, 13, 54]
	print ("Given array is", end ="\n") 
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end ="\n") 
	printList(arr) 


'''
Result
======
Given array is
17 87 6 22 41 3 13 54 
Sorted array is: 
3 6 13 17 22 41 54 87 
'''