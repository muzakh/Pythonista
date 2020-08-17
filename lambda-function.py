"""
Lambda function 
================
lamdba arguments : expression

where:
    arguments : more than one possible
    expression : can only be one
"""


def double(x):
    return x * 2

def tripple(x):
    return x * 3

print(double(11))
print(tripple(11))



'''

Another Example from:
https://thepythonguru.com/python-lambda-function/#:~:text=Python%20allows%20you%20to%20create,not%20more%20than%20a%20line.&text=The%20result%20of%20the%20expression,is%20applied%20to%20an%20argument.


Python allows you to create anonymous function i.e function having no names using a facility called lambda function.

Lambda functions are small functions usually not more than a line. It can have any number of arguments just like a normal function. The body of lambda functions is very small and consists of only one expression. The result of the expression is the value when the lambda is applied to an argument. Also there is no need for any return statement in lambda function.

Let's take an example:

Consider a function multiply():

'''



def multiply(x, y):
    return x * y

# OR

r = lambda x, y: x * y
print(r(12, 3))   # call the lambda function

# OR

(lambda x, y: x * y)(3,4)

