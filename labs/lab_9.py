'''
Lab 9: A program that makes a list from 3 random numbers. It will then total the
list's numbers and determine their average.
'''

print(__doc__)


# Write a program that constructs an empty list and adds 3 numbers to the list.
lst = []

# generate 3 random numbers
import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)

# make a list
lst.append(num1)
lst.append(num2)
lst.append(num3)

# check it twice
print(lst)

# Use a loop to total the elements.
sum_num = 0
i = 0

for i in lst:
    sum_num += i
    i += 1

# Then print the total.
print("Total: {}".format(sum_num))
# print the average
print("Average: {:.2f}".format(sum_num / len(lst)))
