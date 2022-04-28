# Include a module docstring that summarizes the program.
'''This program has the Python, Inc. employee enter their name, hours worked,
and pay rate. Their pay, including over-time pay, is calculated and displayed.
'''

print(__doc__)

# Prompt the user for a name
name = input("Enter employee name: ")

# Prompt the user for hours worked
time = float(input("Enter hours worked: "))

# Prompt the user for hourly rate
rate = float(input("Enter hourly rate: "))

# If the employee works over 40 hours, they should receive 1.5 times their
# hourly rate for all hours worked over 40.

if time <= 40:
    pay = time * rate
else:
    # find the amount of overtime hours worked
    overtime = time % 40
    # calculate the extra page for overtime
    overrate = rate * .5
    #calculate the net pay
    pay = (time * rate) + (overtime * overrate)


paycheck = pay

# Print the employee name and the amount the employee should be paid.
# Display the payment amount with two digits after the decimal place and commas.

print()
print("{} should be paid ${:,.2f}.".format(name, pay))

## SAMPLE RUN

## Enter a name: Guido van Rossum
## Enter hours worked: 42.5
## Enter hourly rate: 285.11
## Guido van Rossum should be paid $12,473.56
