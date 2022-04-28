'''
Homework 8: Write a function that takes two arguments, both strings. Print "YES"
if the second string argument contains only characters found in the first string
argument. Print "NO" if the second string argument contains characters not in
the first. (expect YES, YES, NO)
'''

print(__doc__)

def makeStr(args1: str, args2: str) -> str:

    ''' Prints "YES" if the second string argument contains only characters
    found in the first string argument. Prints "NO" if the second string
    argument contains characters not in the first.'''

    if len(args2) > 0: # check if there are char in str 2 to check still 
        if args2[0] in args1: # check if the first char of str 2 is in str 1
            makeStr(args1, args2[1:])
            # slice str 2 by the first char and recurse the function
        else:
            print("NO") # if a char is not found in str 1, print NO
    else:
        print("YES") # if all char in str 2 are in str 1, print YES
    
# example calls and their expected results
makeStr("hello", "") # YES
makeStr("hello", "olleloheloeloheloel") # YES
makeStr("hello", "olleloheloteloheloel") # NO
