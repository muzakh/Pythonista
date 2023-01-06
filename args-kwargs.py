
def printingData(codeName, *args, **kwargs):
    print("Code is: {}" . format(codeName))
    for x in args:
        print("I am arg: {} ". format(x))
    for y in kwargs.items():
        print("I am kwargs: {}" . format(y))

print(printingData('007', 'agent', FirstName='James', LastName='Bond'))


def multipleCalculator(*numbers):
    product = 1
    for x in numbers:
        product = product * x
    return product

print(multipleCalculator(1,3,2))

# Unpacking Iterables using args and kwags

carsList = ['Audi','BMW','Lamborghini']
print(*carsList)

adict = {"React": "Facebook", "Angular" : "Google", "dotNET" : "Microsoft"}
adict2 = {"java": "Netflix"}
merged = {**adict, **adict2}
print(merged)



Output:
-------
Code is: 007
I am arg: agent 
I am kwargs: ('FirstName', 'James')
I am kwargs: ('LastName', 'Bond')
None
6
Audi BMW Lamborghini
{'React': 'Facebook', 'Angular': 'Google', 'dotNET': 'Microsoft', 'java': 'Netflix'}
