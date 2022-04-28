## refer to the word counter in end of Lecture10Dictionaries.py

'''
Homework 10: The function takes a string argument and will create a dictionary.
Iterate through the string and store the letter frequency in the dictionary
created. The key will be the letter and the value will be the number of times
the letter occurs in the word. Print the dictionary.
'''

print(__doc__)

# Write a function that takes a string argument.

def charCount(word: str) -> dict:

    # convert word to lower case
    word = word.lower()
    
    # The function should create a dictionary.
    chars = dict()

    # Iterate through the string and store the letter frequency in the
    # dictionary you created.
    for char in word:
        # if the char is in the word, increment count
        if char in chars:
            chars[char] += 1
        # if the char is NOT in the word, add it with count = 1
        else: chars[char] = 1
        
    # Print the dictionary.
    print(chars)

charCount(input("Please enter a string: "))

# EXAMPLES

##charCount("happy")
# {'h': 1, 'a': 1, 'p': 2, 'y': 1}

##charCount("AaBbCc")
# {'a': 2, 'b': 2, 'c': 2}

##charCount("pneumonoultramicroscopicsilicovolcanoconiosis")
# {'p': 2, 'n': 4, 'e': 1, 'u': 2, 'm': 2, 'o': 9, 'l': 3, 't': 1, 'r': 2,
# 'a': 2, 'i': 6, 'c': 6, 's': 4, 'v': 1}
