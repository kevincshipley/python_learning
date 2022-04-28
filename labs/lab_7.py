'''
Lab 7: This program will prompt the user for two integers. It will then return
the minimum of the first integer and 0, and then the minimum of the two integers
entered by the user.
'''

print(__doc__)

# Write a function called min2 that takes two arguments.
# The second argument should be a default argument with a default value of 0.

def min2(args1, args2=0):

    # The function will RETURN the minimum of the 2 arguments.
    return min(args1, args2)

# Prompt the user for two integers.

x = int(input("Enter an integer: "))
y = int(input("Enter an integer: "))
          
# Call the function with the first number typed and no second argument.
# Print the results. 

print("The minimum of {:,} and {:,} is {:,}.".format(x, 0, min2(x)))

# Call the function again with both numbers the user types.
# Print the results.

print("The minimum of {:,} and {:,} is {:,}.".format(x, y, min2(x, y)))
