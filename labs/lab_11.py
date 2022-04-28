# You will write two functions. Follow the format given below. Call both
# functions and verify they work correctly.

# Function 1 – Write a function that opens a file for writing and writes to the
# file. The function should take a string as an argument. The string will be a
# file name. Open a file with that name for writing. Write your name, major,
# and favorite hobby to that file on separate lines (3 lines). Close the file.
# No return value is needed.

def studentInfo(fileName: str):
    openfile = open(fileName, "w")
    # Write your name, major, and favorite hobby to that file on separate lines
    print("Kevin Shipley", "Computer Science", "Board games", sep="\n",
          file=openfile)
    # close the file, no return value
    openfile.close()

studentInfo("student_info.txt")

# Function 2 – Write a function that opens a file for reading. The function
# should take a string as an argument. (If your function has empty parentheses,
# you will be marked down.) The string will be a file name. Open a file with
# that name for reading. Read the contents of the file and print the file
# content to the screen.

def readInfo(fileName: str):
    openfile = open(fileName, "r")
    print(openfile.read())

readInfo("student_info.txt")
