# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 02:48:28 2020

@author: Hp

Description : Crating Super and sub classes along with __str__ and __repr__ magic string functions
"""

class Vehicle(object):
    def __int__(self, year, make, model):
        ''' Defines a class '''
        self.year = str(year)
        self.make = make
        self.model = model
        self.NumberPlate = 'XYZ-012'
    
    def __str__(self):
        ''' Defines string representation of class in order to ensure its output compatibility with strings '''
        return "String representation : Year:{0}, Make;{1} and Model:{2}" . format(self.year, self.make, self.model)
    
    def __repr__(self):
        ''' __repr__ does the same as __str__ dunder/magic function does but it instead is a more formal form of string representation'''
        return "String representation : Year:{0}, Make;{1} and Model:{2}" . format(self.year, self.make, self.model)
    
    def __add__(self, b):
        ''' This is to perform the addition. Only invoked it for testing '''
        return self.make + self.year + self.model + b.year
    
    def printVehicle(self):
        ''' A method used to print the Year, Make and Model of the car '''
        print("Number Plate is : " . foramt(self.NumberPlate))
        print("Year:{0}, Make;{1} and Model:{2}" . format(self.year, self.make, self.model))


''' Defining a SubClass called Truck from the SuperClass: Vehicle'''
class Truck(Vehicle):
    pass



if __name__ == '__main__':
    car = Vehicle("2006", "Suzuki", "Cultus")
    motorcycle = Vehicle("2017", "Super Power", "70")
    print(car)
    
    print(motorcycle)
    print(motorcycle.year)
    print(motorcycle.make)
    print(motorcycle.model)
    print(motorcycle.NumberPlate)
    
    print("Now Overriding the attributes of motorcycle class: \n")
    
    motorcycle.model = "Leoncino 800"
    motorcycle.make = "Benelli"
    motorcycle.year = "2020"
    print(motorcycle)
    
    print("\n" * 2)
    
    Truck.make = "Hyundai"
    Truck.model = "Shehzore"
    print("Truck is : {0} amd {1}" . format(Truck.make, Truck.model))
    
    help(Vehicle.printVehicle)
    help(Vehicle.make)
    
    
    