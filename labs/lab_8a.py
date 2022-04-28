'''
Lab 8a: This program returns the same result as the built-in partition method
for strings.
'''

print(__doc__)

# Write a function that returns the same result as the built-in partition method
# for strings. Your function will take two arguments, both strings.

def split_it_up(a_string: str, sep: str):
    # a_string: the string to partition
    # sep: the separator string
    i = a_string.find(sep)

    # Split the string at the first occurrence of sep
    if i >= 0:
        # return a 3-tuple containing the part before the separator, the separator
        # itself, and the part after the separator.
        return a_string[:i], sep, a_string[i + len(sep):]
    
    # If the separator is not found, return a 3-tuple containing the string
    # itself, followed by two empty strings.
    else:
        return a_string, "", ""

print(split_it_up("hello world", " "))
## ('hello', ' ', 'world')

print(split_it_up("hello world", "wo"))
## ('hello ', 'wo', 'rld')

print(split_it_up("hello world", "r"))
## ('hello wo', 'r', 'ld')

print(split_it_up("hello world, I am ready to program", " "))
## ('hello', ' ', 'world, I am ready to program')

print(split_it_up("hello world", "|"))
## ('hello world', '', '')
