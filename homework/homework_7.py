'''
Homework 7: Calling the function avg() will calculate and return the average of
the arguments entered.
'''
print(__doc__)

# Write a function that takes a variable length argument list.
def avg(*args):

    # In the function body, calculate and return the average of the arguments.
    total = 0
    for num in args:
        total += num
    # If the function is called without any arguments return None.
    if len(args) == 0:
        return None
    else:
        return total / len(args)

# Call the function twice.

# One call will include numeric arguments of your choosing.
print(avg(5, 10, 15)) # 10.0

# One will have have an empty argument list.
print(avg()) # None
