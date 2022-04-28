'''
Players will guess a number from 1 to 10, and the closest guess wins.
'''

print(__doc__)

# Prompt two users to guess the number.
mario = int(input("Player 1, enter a number from 1 to 10: "))
luigi = int(input("Player 2, enter a number from 1 to 10: "))

# generate a random number from 1 to 10, including 1 and 10
import random
num = random.randint(1, 10)
print("Magic Number: {}".format(num))


# calculate difference
marionum = abs(num - mario)
luiginum = abs(num - luigi)

# Identify which guess is closest.
if marionum < luiginum:
    print("Player 1 guessed {} which is closer to {} than {}."
          "".format(mario, num, luigi))
elif marionum > luiginum:
    print("Player 2 guessed {} which is closer to {} than {}."
          "".format(luigi, num, mario))
else:
    marionum == luiginum
    print("Sorry, there was no winner.")


# If both guesses are equally close, print stating there are no winners.

# You will likely have to use abs() which calculates the absolute value
# of the argument. bs(5) = 5, abs(-5) = 5, abs(0) = 0.

# You can assume ideal input – users will not type the same guess.

# HINT: Print the random number before prompting the users so the
# program is easier to debug.
