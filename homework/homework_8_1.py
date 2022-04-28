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
    
    inStr = True
    
    for char in args2:
        if char not in args1:
            inStr = False
            break
        else:
            inStr = True

    if inStr == True:
        print("YES")
    else:
        print("NO")
            
    
# example calls and their expected results
makeStr("hello", "") # YES
makeStr("hello", "olleloheloeloheloel") # YES
makeStr("hello", "olleloheloteloheloel") # NO
