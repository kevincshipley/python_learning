# Write a function, is_valid_RN, which validates ABA (American Banker's
# Association) routing numbers.

# The function takes 1 argument, a string representation of a routing number,
# and returns True if the number is valid and False otherwise.
def is_valid_RN(r_num: str) -> bool:

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

print(is_valid_RN("abc")) # Not a number, False
print(is_valid_RN("123")) # Wrong length, False
print(is_valid_RN("789456124")) # True
print(is_valid_RN("789456125")) # False

##Enter routing number: 789456124
##789456124 is valid
##Enter routing number: 789456125
##789456125 is invalid
