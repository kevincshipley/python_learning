'''
Homework 9: Prompts user to enter a nonnegative integer and adds it to a list.
The list is then totaled and printed when the user is completed entering input.
'''

print(__doc__)

# Write a function that returns a list of numbers, will not take any arguments.
def make_list() -> list:
    
    '''prompts the user for numbers, adding them to a list, and then returns
    the list when the user chooses to quit'''
    
    # construct an empty list
    lst = []
    num = 0
    while num != -999:
    # prompt the user to enter a nonnegative number, -999 to quit
        num = int(input("Enter a nonnegative integer, -999 to quit: "))
        # Once the user enters -999, quit the loop
        if int(num) == -999:
            break
        elif int(num) <0:
        # If the user enters a number other than -999, add it to the list.
            print("Please try again...")
            continue
        else:
            lst.append(num)
    # return the list
    return lst

# Write another function that takes a list of numbers as an argument
def sum_list(args: list) -> sum:

    '''takes a list of numbers and returns an argument'''
    
    # If the list is empty return 0.
    if args == []:
        return 0
    else:
        lst_total = 0
        for num in args:
            lst_total += num
        # returns the sum of the list of numbers.
        return lst_total

# You need to call both functions.

# First call the make_list function.
lst = make_list()

# Then use the returned list as the argument for the sum_list function.
print("\nThe total of {} is {:,}.".format(lst, sum_list(lst)))
