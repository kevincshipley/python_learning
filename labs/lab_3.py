'''
Create a list or tuple with 5 different integers. Prompt the user for an
integer. If the number is in the list (or tuple) print a message stating the
number was found. Otherwise, print a message stating the number was not found.

Assume the list (or tuple) includes the numbers 2, 4, 6, 8, and 10.

'''
print(__doc__)

# list of 5 different integers
numbers = [2, 4, 6, 8, 10]

# Prompt the user for an integer.

integer = input("Please enter an integer: ")

# If the number is in the list (or tuple) print a message stating the number
# was found. Otherwise, print a message stating the number was not found.

if integer in numbers:
    print("\n{} is in the list.".format(integer))
else:
    print("\n{} is not in the list.".format(integer))

