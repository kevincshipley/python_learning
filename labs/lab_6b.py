'''
Lab 6b: This program will prompt the user for a string, and then will print the
index, a colon, and the character at that index.
'''

print(__doc__)

def print_it(spelling):

    for count, letter in enumerate(spelling):
        # prints the index, a colon, and the character at that index.
        print("{}: {}".format(count, letter))

# Prompt the user for a string and call the function with the string the user
# enters as an argument.
word = input("Please enter a string: ")

print()
print_it(word)
