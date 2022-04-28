'''
Lab 5b: This program will prompt the user for a positivte integer. It will
calculate all even integers entered. Once the user enters an integer that is 0
or lower, the program will print the sum of the positive even integers entered.
'''

print(__doc__)

# Write a sentinel-controlled loop that prompts for positive integers.

# Once the user types the sentinel value, exit the loop and print the sum.
# The sentinel value should not be included in the sum.

# The program should calculate the sum of all even numbers entered.

totaleven = 0
num = 1

while num > 0:
    num = int(input("Enter a positive integer(<= 0 to quit): "))
    
    if num % 2 == 0:
        totaleven += num
    elif num <= 0:
        break
    else:
        continue

print("The sum of the positive integers entered is {}.".format(totaleven))
