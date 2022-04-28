'''
Homework 5: This program asks the user to input the amount of gallons in a
tankful of fuel, followed by the miles they drove on that tankful. Once the user
is completed entering their tankfuls, the program will calculate and display
their average miles per gallon.
'''
print(__doc__)

# Drivers are concerned with the mileage obtained by their automobiles.

# One driver has kept track of several tankfuls of gasoline by recording
# gallons used and miles driven for each tankful.

# Develop a program that will input the gallons used and miles driven for each
# tankful (-1 to quit).

# The program should calculate and display the miles per gallon obtained for
# each tankful.

# After processing all input information, the program should calculate and
# print the combined miles per gallon obtained for all tankfuls.

total_mil = 0
total_gal = 0

while True:
    # input gallons used
    gallons = float(input("Enter gallons used (-1 to quit): "))
    if gallons >= 0:
        # input miles driven for each tankful, -1 to quit
        miles = float(input("Enter miles driven: "))
        # calculate and print the mpg for each tankful
        mpg = miles / gallons
        print("MPG: {:,.2f}\n".format(mpg))
        # keep track of the total mpg
        total_mil += miles
        total_gal += gallons
        continue
    else:
        total_mpg = total_mil / total_gal
        print("\nAverage MPG: {:,.2f}".format(total_mpg))
        break
