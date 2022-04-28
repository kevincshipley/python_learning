'''
Lab 2b: Write a Python program that prompts the user for a measurement in inches.
Convert the user input into the equivalent measurement in centimeters
(1 inch = 2.54 cm). Print the converted value.
'''

print(__doc__)

# ask for input in inches
measure_inch = float(input("Please enter a number of inches: "))

# convert the input to centimeters (1 inch = 2.54 cm)
measure_cent = measure_inch * 2.54

# print the converted value
print(measure_inch, "inches is equal to", measure_cent, "centimeters.")
