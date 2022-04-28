'''
Welcome Python Inc. employee...

This program is used to calculate the pay for employees entered, as well as to
calculate the average and total amount of pay to those entered employees.
'''

print(__doc__)

################################################################################

## FUNCTION 1

def get_input():

    '''Prompts for name, hours, and rate. Returns the name (str), hours worked
    (float), and hourly rate (float) for one employee.'''

    # Prompt the user for employee's name
    emp_name = str(input("Enter employee name: "))
    
    # Prompt the user for hours worked
    emp_hours = float(input("Enter hours worked: "))
    
    # Prompt the user for hourly rate
    emp_rate = float(input("Enter hourly rate: "))

    return emp_name, emp_hours, emp_rate
    
################################################################################

## FUNCTION 2

def calc_pay(pay_hours: int, pay_rate: float) -> float:

    '''Returns the amount the employee gets paid for the week. If the employee 
    works over 40 hours, they should receive 1.5 times their hourly rate for all
    hours worked over 40.'''

    # determine base pay
    pay = pay_hours * pay_rate
    # determine if overtime was worked
    if pay_hours > 40:
        # determine overtime hours
        overtime = pay_hours % 40
        # determine overtime pay
        pay += overtime * (pay_rate * .5)

    return pay

################################################################################

if __name__ == "__main__":

    # Ask for number of employees to be entered
    employees = int(input("How many employees do you want to enter? "))
    print()

    # define global variable
    entries = employees
    total_pay = 0
    total_hours = 0

    # loop to enter each employee info
    while entries > 0:
        # get employee name, hours worked, pay rate
        name, hours, rate = get_input()
        # calculate employee's paycheck
        paycheck = calc_pay(hours, rate)
        # print the employee's name and how much they should be paid
        print("{} should be paid ${:,.2f}".format(name, paycheck))
        print()
        # track total pay
        total_pay += paycheck
        # track total hours
        total_hours += hours
        # track how many employees left to enter
        entries -= 1
        
    # when done entering employees, return the total amoun to be paid
    print("The total amount to be paid is ${:,.2f}".format(total_pay))
    # return the average pay for employees entered
    print("The average employee is paid ${:,.2f}".format(total_pay / employees))

################################################################################
