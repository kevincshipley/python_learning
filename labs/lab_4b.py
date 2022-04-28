'''
Enter two choices, and the program will flip a coin to select one of them.
'''

print(__doc__)

import random

# You are going to implement a coin flipping program.

# Prompt the user for two choices.

heads = input("Enter choice 1: ")
tails = input("Enter choice 2: ")

coin = [heads, tails]

# Then select a choice based on a random number. Print the choice selected.
print(random.choice(coin))
