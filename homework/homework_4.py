'''
This program will generate a random integer from 0-99, prompts the user to enter
an integer in that range, and then lets them know how much money they won.
'''

print(__doc__)

import random
from random import randint

# randomly generates an integer from 0-99
number = random.randint(0, 99)
print(number)

# prompts the user to enter an integer from 0-99
ticket = int(input("Enter and integer from 0-99: "))


# If the user's input matches the lottery number in the exact order, the award
# is $10,000

if number == ticket:
    winnings = "10,000!"


# If all the digits in the user's input match all the digits in the lottery
# number but in a different order, the award is $3,000

# num // 10 gets tens digit, Integers 0-9 have a 0 in the tens place.
# num % 10 gets ones digit. 

elif number // 10 == ticket % 10 and number % 10 == ticket // 10:
    winnings = "3,000!"

# If only one digit in the user's input matches a digit in the lottery number,
# the award is $1,000

elif number // 10 == ticket % 10 or number % 10 == ticket // 10 or number % 10 == ticket % 10 or number // 10 == ticket // 10:
    winnings = "1,000!"

else:
    winnings = "0..."

# prints out how much is won according to the previous rules
print("You won ${}".format(winnings))
