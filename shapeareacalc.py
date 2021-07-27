"""This program is an area calculator for squares, rectangles, triangles, and circles"""
"""To make this program we will use classes for each shape"""
"""Final program will have user choose shape and input the dimensions"""

#library that will import the value of PI
import math 

class Rectangular(object):
    def __init__(self, length, width):
            self.length = length
            self.width = width
    def area(self):
        return self.width * self.length

length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
r = Rectangular(length, width)
print("Area of Rectangle is", (r.area()))

class Square(object):
    def __init__(self, side):
        self.side = side
    def sqaurearea(self):
        return (math.pow(self.side, 2))
side = int(input("Enter side length of square: "))
s = Square(side)
print("Area of Square is", (s.sqaurearea()))

class Circle(object):

    def __init__(self, radius):
        self.radius = radius
    def circulararea(self):
        return math.pi * (math.pow(self.radius, 2))

diameter = int(input("Enter Diameter of circle: "))
radius = diameter/2
c = Circle(radius)
print("Area of a circle is", (c.circulararea()))

class Triangle(object):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def triangulararea(self):
        ta = (self.base * self.height)/2
        return ta
   
base = int(input("Enter Base of Triangle: "))
height = int(input("Enter Height of Triangle: "))
t = Triangle(base, height)
print("Area of a Triangle is", (t.triangulararea()))