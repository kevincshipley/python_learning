'''Homework 2: Write a Python program that prompts a user for two integers
and stores the two integers the user types into the shell. Print the product,
float division, integer division, remainder, sum, and difference of the two
integers to the console. The entire equation must be printed (see below for
formatting). Only display 2 digits after the decimal place for results that
are floats.'''

print(__doc__)

# prompt user for two integers and store the two integers

int_1 = int(input("\nEnter an integer: "))

int_2 = int(input("\nEnter another integer: "))

# Print the product of the two int, *
print()
operator = "*"
result = int_1 * int_2
print("{} {} {} = {}".format(int_1, operator, int_2, result))

# Print the float division of the two int, /
# this is the only result that will be a float if both are int, see p. 36
print()
operator = "/"
result = int_1 / int_2
if result - int(result) == 0:
    print("{} {} {} = {}".format(int_1, operator, int_2, int_1 // int_2))
else:
    result = float(format(int_1 / int_2, '.2f'))
    print("{} {} {} = {}".format(int_1, operator, int_2, result))

# Print the integer division of the two int, //
print()
operator = "//"
result = int_1 // int_2
print("{} {} {} = {}".format(int_1, operator, int_2, int_1 // int_2))

# Print the remainder of the two int, %
print()
operator = "%"
result = int_1 % int_2
print("{} {} {} = {}".format(int_1, operator, int_2, result))

# Print the sum of the two int, +
print()
operator = "+"
result = int_1 + int_2
print("{} {} {} = {}".format(int_1, operator, int_2, result))

# Print the difference of the two int, -
print()
operator = "-"
result = int_1 - int_2
print("{} {} {} = {}".format(int_1, operator, int_2, result))
