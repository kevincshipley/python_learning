'''
Homework 8: Write a function that takes two arguments, both strings. Print "YES"
if the second string argument contains only characters found in the first string
argument. Print "NO" if the second string argument contains characters not in
the first. (expect YES, YES, NO)
'''

print(__doc__)

def makeStr(args1: str, args2: str) -> str:

    ''' Print "YES" if the second string argument contains only characters found
    in the first string argument. Print "NO" if the second string argument
    contains characters not in the first.'''

    i = 0
    inStr = True
    
    while i < len(args2):
        if args2[i] in args1: # if char at index i is in args1, loop continues
            i += 1
        elif args2[i] not in args1: # if char at index i is not in args1, breaks
            inStr = False
            break

    # if all char in args2 were found in args1, prints "YES"
    if inStr == True:
        print("YES")
    # if ANY char in args2 were NOT found in args1, prints "NO"
    else:
        print("NO")


# This does NOT have to be a recursive function.

# example calls and their expected results
makeStr("hello", "") # YES
makeStr("hello", "olleloheloeloheloel") # YES
makeStr("hello", "olleloheloteloheloel") # NO
