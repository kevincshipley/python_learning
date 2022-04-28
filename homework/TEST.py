lst = []
num = 0
while num != -999:
# prompt the user to enter a nonnegative number, -999 to quit
    num = input("Enter a nonnegative number, -999 to quit: ")
    # Once the user enters -999, quit the loop
    if num == -999:
        break
    # If the user enters a number other than -999, add it to the list.
    else:
         lst.append(num)
# return the list
print(lst)
