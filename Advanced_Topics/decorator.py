# https://www.datacamp.com/tutorial/decorators-python

import functools

def split_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func().split()
    return wrapper

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@split_decorator
@uppercase_decorator
def sayHello():
    return "Hello there"

print(sayHello())

'''
Output:
========
['HELLO', 'THERE']
'''

print("\n")
################################################

def a_function_to_decorate(func):
    @functools.wraps(func)
    def wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Positional arguments: {}" . format(args))
        print("Keyword arguments: {}" . format(kwargs))
        return func(*args)
    
    return wrapper_accepting_arbitrary_arguments

@a_function_to_decorate
def func_with_no_arguments(x, y):
    return "Arguments are {}, {}" . format(x, y)

print(func_with_no_arguments(3, 4))

'''
Output:
========
Positional arguments: (3, 4)
Keyword arguments: {}
Arguments are 3, 4
'''
