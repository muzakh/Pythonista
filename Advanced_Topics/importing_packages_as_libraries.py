# -*- coding: utf-8 -*-
"""
Testing the functionality of __name__ == '__main__' 
Test by doing import square and it will not return the output. It will only import it as a library:

import importing_packages_as_libraries
importing_packages_as_libraries.square(2)
Out[6]: 4

"""


def square(x):
    return x * x

if __name__ == '__main__':
    inp = int(input("Enter number: "))
    print('Square of {0} is : {1}' . format(inp, square(inp)))

