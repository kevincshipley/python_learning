'''Homework 11: Prompts the user to enter the names of students in a class.
The program will then names of the students, and how many have each name
entered. (User will enter "q" to stop entering names.)'''

print(__doc__)

print()

def names():

    '''Implement function names() that takes no arguments and repeatedly asks
    the user to enter the first name of a student in a class.'''
    
    student = input("Enter student name: ")
    classList = {}
    
    while student != "q":
        if student in classList:
            classList[student] += 1
        else:
            classList[student] = 1
        
        student = input("Enter next name: ")

    # When the user enters q, the function should print for every name the
    # number of students with that name.
    for name, count in classList.items():
        print("{} student(s) named {}".format(count, name))
    
# Call the function to test.
names()

##import sys
##sys.stdin = open("hw11.txt")
##sys.stdin.names()

# automate testing (not required)
# import sys
# sys.stdin
# sys.stdin = open(filename.txt)
# have the test input in a file, get it from file instead of screen
