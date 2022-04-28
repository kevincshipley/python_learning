'''
Lab 6a: This program calculates the factorials of 5 and 20.
'''

print(__doc__)

# Write a function that takes an integer argument and returns the factorial of
# that argument.

# Return DOES NOT mean print. Include a return statement.

# Invoke/Call the function twice with arguments of your choice
# (positive integers) and print the result.

# The function is similar to the sum_to function shown in class.

# Do NOT use any built-in factorial function.

# calculate factorial of given integer "n"
def factorial(n):
    
    count = 1
    fact = n
    
    while count <= n - 1:
        fact *= count
        count += 1
    else:
        return fact

# Print the factorial
def factprint(n):

    fact = factorial(n)
    print("The factorial of {:,} is {:,}.".format(n, fact))

# Invoke the factorial fucntion created
factprint(5)

factprint(20)
