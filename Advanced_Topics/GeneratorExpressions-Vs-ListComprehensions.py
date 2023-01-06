"""
Created on Sun Apr 12 20:44:55 2020

@author: Zohaib
Decription: List comprehension Vs Generator Expressions

List Comprehension : Generates a list using for loop. Written in square brackets and returns a complete list. Memory hungry.

Generator Expression : Returns element of a list one by one. Syntax is same as that of list comprehensions but its written in small brackets.Memory efficient
"""

interator = 11

""" List Comprehension """
# Calsulates square of nunbers within given range of numbers greater than 5
alist = [i**2 for i in range(interator) if i > 5]
print(alist)
print("Data type is a : " + str(type(alist)))

""" Generator Expressions """
# Calsulates square of nunbers within given range of numbers greater than 5

def gen_exp_fn():
    return (i**2 for i in range(interator) if i > 5)

gen_exp = gen_exp_fn()
print("\nGenerator Function has {0}" . format(gen_exp))

print(type(gen_exp))

''' Now printing the values of a generator or developing a list from the generator func using a for loop'''
print("\n\n *** Applying Generator Function again to refresh generator object and fetching elements one by one using the loop ***\n")
gen_exp = gen_exp_fn()

for var in gen_exp:
    print(var)
    
    
    


def my_generator(n):
    count = 0
    while count < n:
        yield count
        count += 1


for x in my_generator(3):
    print(x)


print("\n" * 2)

squares_generator_fn = (x*x for x in range(5))

for y in squares_generator_fn:
    print(y)


Output:
-------
0
1
2


0
1
4
9
16


