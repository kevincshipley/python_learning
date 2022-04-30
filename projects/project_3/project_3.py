'''
Project 3: This program will prompt for Credit Card Numbers and then Routing
Numbers. It will determine if the entered number is valid, and then prompt for
further input.
'''

print(__doc__)

## Do NOT use global variables in either function. ##

def luhn(cc_num: str) -> bool:

    '''This function uses the luhn algorithm to determine validity'''

    #1. Starting with the rightmost digit, add every other digit.
    sum1 = 0
    for digit in cc_num[-1::-2]:
        value = int(digit)
        sum1 += value
        
    #2. Double every other digit starting with the second digit from the right.
    # If doubling of a digit results in a two-digit number, add the two digits
    # to get a single-digit number.
    sum2 = 0
    for digit in cc_num[-2::-2]:
        value = int(digit) * 2 # doubles every other digit as int
        value = str(value) # converts to string
        if len(value) == 2: # if value is 2 digits, add them together
            digit1 = int(value[0])
            digit2 = int(value[1])
            value = int(digit1) + int(digit2) # add as int
        else:
            value = int(value)
        sum2 += value

    #3. Sum the results from Steps 1 and 2.
    total = sum1 + sum2

    #4. If the result from step 3 is divisible by 10, the credit card number
    # is valid. Otherwise the number is invalid.
    if total % 10 == 0:
        return True
    else:
        return False

# Write a function, is_valid_CC, that validates credit card numbers.

def is_valid_CC(cc_num: str) -> bool:

    '''This function takes 1 argument, a string representation of a credit card
    number, and returns True if the number is valid and False otherwise.'''

    # You also have to verify the number using the Luhn algorithm.
    if luhn(cc_num):
        # A valid credit card is a number containing only digits 0-9.
        if cc_num.isdecimal():
           # The length is between 13 – 16 digits
            if len(cc_num) <= 16 and len(cc_num) >= 13:
                # starts with a: 4 (Visa)
                if cc_num[0] == "4":
                    card_type = "Visa"
                # starts with a: 5 (MasterCard)
                elif cc_num[0] == "5":
                    card_type = "Mastercard"
                # starts with a: 6 (Discover)
                elif cc_num[0] == "6":
                    card_type = "Discover"
                # starts with a: 37 (American Express)
                elif cc_num[0] == "3" and cc_num[1] == "7":
                    card_type = "American Express"
                else:
                    return False
                return True
    else:
        return False

##cc_num = "4388576018402626"
##valid_cc, cc_type = is_valid_CC(cc_num) # (False, 'Visa')
##
##cc_num = "4388576018410707"
##valid_cc, cc_type = is_valid_CC(cc_num) # (True, 'Visa')

################################################################################

# Write a function, is_valid_RN, which validates ABA (American Banker's
# Association) routing numbers.

# The function takes 1 argument, a string representation of a routing number,
# and returns True if the number is valid and False otherwise.
def is_valid_RN(r_num: str) -> bool:
    
    '''The function takes 1 argument, a string representation of a routing
    number, and returns True if the number is valid and False otherwise.'''

    # A valid routing number is a number containing only digits 0-9 that is
    # exactly 9 digits long.
    for digit in r_num:
        if digit not in "0123456789":
            print("Not a number")
            return False
    if len(r_num) != 9:
        print("Wrong length")
        return False
    
    # You also have to verify the number using the following algorithm.
    
    #1. Starting with the rightmost digit, add every third digit.
    sum1 = 0
    for digit in r_num[-1::-3]: # start with the rightmost digit
        sum1 += int(digit) # add every third digit
    
    #2. Starting with the second digit from the right, add every third digit and
    # multiply the result by 7.
    sum2 = 0
    for digit in r_num[-2::-3]: # start with second digit from the right
        sum2 += int(digit) # add every third digit
        sum2 *= 7 # multiply the result by 7
    
    #3. Starting with the third digit from the right, add every third digit and
    # multiply the result by 3.
    sum3 = 0
    for digit in r_num[-3::-3]: # start with third digit from the right
        sum3 += int(digit) # add every third digit
        sum3 *= 3 # multiply the result by 3
    
    #4. Sum the results from Steps 1 – 3.
    total = sum1 + sum2 + sum3
    
    #5. If the result from step 4 is divisible by 10, the routing number is
    # valid. Otherwise the number is invalid.
    if total % 10 == 0:
        return True
    else:
        return False
    
################################################################################
    
print("Credit Card Entry")
print("-----------------------------------------------------------------------"
      "---------")

# Your test code should include a loop that prompts for a credit card number
# or q to quit.
card_num = input("Enter credit card number (q to quit): ")

# If the user types q, the loop should be terminated.
while card_num != "q":
    
    # If the user enters a credit card number, print a statement whether it is
    # valid and prompt for another credit card number.
    if is_valid_CC(card_num):
        print("{} is valid.".format(card_num))
    else:
        print("{} is invalid".format(card_num))

    card_num = input("Enter credit card number: ")

print("\nRouting Number Entry")
print("-----------------------------------------------------------------------"
      "---------")

# Do the same for routing numbers - Include loop that prompts for a routing
# number or q to quit.
routing = input("Enter routing number (q to quit): ")

# If the user types q, the loop should be terminated.
while routing!= "q":
      
# If the user enters a routing number, print a statement whether it is valid
# and prompt for another routing number.
    if is_valid_RN(routing):
        print("{} is valid.".format(routing))
    else:
        print("{} is invalid.".format(routing))

    routing = input("Enter routing number (q to quit): ")

################################################################################

'''
Sample Run:

Credit Card Entry
--------------------------------------------------------------------------------
Enter credit card number: 4388576018410707
4388576018410707 is valid
Enter credit card number: 4388576018402626
4388576018402626 is invalid
Enter credit card number: q

Routing Number Entry
--------------------------------------------------------------------------------
Enter routing number: 789456124
789456124 is valid
Enter routing number: 789456125
789456125 is invalid
Enter routing number: q
'''
