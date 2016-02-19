# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:03:36 2016

@author: Craig
"""

# create a new object type called Sample
class Sample(object):
    pass

# Instance of a sample
x = Sample()

print type(x)

#  Creating attributes in the special method __init__
class Dog(object):
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
        
sam = Dog(breed = 'Lab', name = 'Sam')
frank = Dog(breed = 'Huskie', name = 'Frank')


# Creating methods within a class
class Circle(object):
    import math
    pi = math.pi
    
    # circle gets instantiated with a radius
    def __init__(self, radius = 1):
        self.radius = radius
    
    # area method to calculate area
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    # method for resetting radius
    def setRadius(self, radius):
        self.radius = radius
    
    # method for getting radius
    def getRadius(self):
        return self.radius
        
    # method for getting circumference
    def circumference(self):
        return 2 * self.radius * Circle.pi
        


# INHERITANCE
class Animal(object):
    def __init__(self):
        print "Animal created"
        
    def whoAmI(self):
        print "Animal"
    
    def eat(self):  # the derived class (dog) inherits functionality of the base class (animal)
        print "Eating"
        
    
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"
        
    def whoAmI(self):  # the derived class modifies existing behavior of the base class
        print "Dog"
    
    def bark(self):
        print "Woof!"
       
       
# SPECIAL METHODS
class Book(object):
    def __init__(self, title, author, pages):
        print "A book is created"
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return "Title: %s, Author: %s, Pages: %s " %(self.title, self.author, self.pages)
        
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print "A book is destroyed"
            
book = Book("Python Rocks!", "Jose Portilla", 159)
    
