## check recording for Week 10 if need explained again

def is_valid_CC(cc_num: str) -> bool:

    if not cc_num.isdecimal():
        print("Not a number")

    if len(cc_num) <= 16 and len(cc_num) >= 13:
        return True

##print(is_valid_CC("45632165478965")) # True
##print(is_valid_CC("12345")) # False
##print(is_valid_CC("abcdefghijklmno")) # "Not a number", True
##print(is_valid_CC("abc")) # "Not a number", False


def luhn(cc_num):

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
            digit2 = int(value[1]))
            sum2 = int(digit1) + int(digit2)
        else:
            sum2 = value

    #3. Sum the results from Steps 1 and 2.
    total = sum1 + sum2

    #4. If the result from step 3 is divisible by 10, the credit card number
    # is valid. Otherwise the number is invalid.
    if total % 10 == 0:
        return True

print(luhn("4388576018402626"))
# True



