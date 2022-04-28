'''Homework 12: This program creates a "triangle" class. Printed below will be
two triangles and their information.'''

print(__doc__)
print()

#Write a class definition for a triangle.
class Triangle:

    # Include a constructor that creates instance variables base and height.
    # The constructor should take two arguments which will be used to set the
    # values of the instance variables base and height.
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height
    
    # Include getters and setters for the instance variables base and height.
    def getBase(self):
        return self.base

    def getHeight(self):
        return self.height

    def setBase(self, base):
        if base > 0:
            self.base = base

    def setHeight(self, height):
        if height > 0:
            self.height = height
    
    # Include a method that returns the area of a triangle. It should refer to
    # the instance variables of base and height. It should not take any
    # arguments. (area = 1/2 * base * height)
    def area(self):
        return 1/2 * self.base * self.height
    
    
# Instantiate a triangle object.
myTriangle = Triangle(2, 4)

print("This is my first Triangle!")
# Print both the base and height using the getters.
print("The base is", myTriangle.getBase())
print("The height is", myTriangle.getHeight())

# Using the setters change the base and height to 5 and 10, respectively.
print("\nAnd this is my second triangle!")

myTriangle.setBase(5)
myTriangle.setHeight(10)

# Then print the area.
print("The area is", myTriangle.area())
