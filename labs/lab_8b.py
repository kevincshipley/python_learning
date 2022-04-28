'''
Lab 8b: A recursive function that takes a positive integer (n) and returns the
sum of the integers from 1 to n.
'''

print(__doc__)

# NOTE: We can add the following two lines to increase Python's recursion depth (1500 can be changed).
import sys
sys.setrecursionlimit(1500)

# Write a recursive function that takes a positive integer, say n, and RETURNS
# the sum of the integers from 1 to n.

# Call your function with an argument of your choice and print the results.

def recurs_fun(n):
    if n == 0:
        return 1
    else:
        return n + recurs_fun(n - 1)

print("The sum from 1 to 123 is {:,}.".format(recurs_fun(123)))
# The sum from 1 to 123 is 7626.
