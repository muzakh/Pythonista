""""
if we dont use __init__ constructor then we have to manually defien the attribute of the class as either blank variable in the class definition
And
Also need to pass the values separatelty at the time of calling the class as shown below:
OR we need to hard-code the value of color and flavor in the class which is least-recommended approach.

jonagold.color = "red"
jonagold.flavor = "sweet"

Constructor makes classes more dynamic by avoiding hard-coding of attributes and also avoids repeated attributes definition at the time of calling the class
""""


class Apple:
    def __init__(self, color, flavor): # __init__ is a spcial method called constructor of a classa and it is called initially when the class is instantiaed 
        self.color = color
        self.flavor = flavor
    def __str__(self): # __str__ method ensures to avoid printing the memory address and instead print below message when the instance of this class is passed to print()
        return "The Apple is {} in color and {} " . format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold.flavor)
print(jonagold)

