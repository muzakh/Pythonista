class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        return "A Class to print the circumference with a given radius of a circle."
    def circumference(self):
        return 2 * 3.142 * self.radius

if __name__ == "__main__":
    circle_1 = Circle(2)
    circle_2 = Circle(4)

    print(circle_1.circumference())
    print(circle_2.circumference())


Output:
------
12.568
25.136

