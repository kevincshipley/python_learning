'''
Lab 5a: This program will take in a positive integer, list out 1 to that number,
and then return the sum of those numbers.
'''
print(__doc__)

# Write a Python program that prompts the user for an integer (positive).

num = range(1, int(input("Please enter a positive integer: ")) + 1)
numsum = 0

# Use a loop to print 1 to the number entered.
# The numbers should appear on the same line separated by spaces.

for i in num:
    print(i, end=" ")
    numsum += i

# On the next line print the sum of the numbers printed on the previous line.

print()
print("The sum is {}.".format(numsum))

# Do not use the built-in sum function or a formula.
# Find the sum using the same loop you use to print the numbers.

