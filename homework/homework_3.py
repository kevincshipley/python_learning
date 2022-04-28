'''
This program takes input as two opposite corners of a rectangle:
the lower left-hand corner (x1, y1) and the upper right-hand corner (x2, y2).
The user will then be prompted for the coordinates of a third point (x, y).
The program will print Boolean value True or False based on whether the
point (x, y) lies within the rectangle.
'''

print(__doc__)

# takes as input two opposite corners of a rectangle:

# the lower left-hand corner (x1, y1)

xy1 = [0,0]
xy1[0] = int(input("Enter x1: "))
xy1[1] = int(input("Enter y1: "))

# the upper right-hand corner (x2, y2)

xy2 = [0,0]
xy2[0] = int(input("Enter x2: "))
xy2[1] = int(input("Enter y2: "))

# the user is prompted for the coordinates of a third point (x, y)S

xy = [0,0]
xy[0] = int(input("Enter x: "))
xy[1] = int(input("Enter y: "))

# The program should print Boolean value True or False based on whether the
# point (x, y) lies within the rectangle.

# if x is in the the rectange, it will be >= x1 and <= x2

# if y is in the rectangle, it will be >= y1 and <= y2

print(xy[0] >= xy1[0] and xy[0] <= xy2[0] and
      xy[1] >= xy1[1] and xy[1] <= xy2[1])
