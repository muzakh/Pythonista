
class Fruit:
    def __init__(self, color, flavour):
        self.color = color
        self.flavour = flavour
    def __str__(self):
        print("This is a Fruit class")


class Apple(Fruit):
    shape = "heart shaped"
    def isay(self):
        return "All apples are not tart in flavour"

class Banana(Fruit):
    shape = "elipse shaped"

apple1 = Apple("red", "tart")
print(apple1.shape, apple1.color, apple1.flavour)

banana1 = Banana("yellow", "sweet")
print(banana1.shape, banana1.color, banana1.flavour)

print(apple1.isay())




Output:
--------
heart shaped red tart
elipse shaped yellow sweet
All apples are not tart in flavour
