'''Homework 14'''

# Create a custom exception class called NegativeIntegerError that inherits
# from ValueError.

class NegativeIntegerError(ValueError):
    # You do not need to implement any code within this class.
    # A pass statement is required if no code is implemented.
    pass

val = input("Enter a non-negative integer: ")

try:
    number = int(val)
    if number < 0:
        raise NegativeIntegerError
    else:
        print("Positive integer entered.")
except NegativeIntegerError as nie:
    print("Negative integer entered.")
except ValueError as ve:
    print("Invalid input.")

# Write a try/except suite.

# In the try, prompt the user for a non-negative integer.
    
# If the integer typed is negative, raise a NegativeIntegerError exception.

# Handle the exception – i.e. Include an except suite that "catches" an
# exception of type NegativeIntegerError.
    
# Also include an except suite that handles the error raised (ValueError) if
# the user types a non-integer when prompted.
# except ValueError as ve:
    
# This error is automatically raised by Python if it cannot convert the
# input to type int.

# Remember to order the except suites appropriately.
