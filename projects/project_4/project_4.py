'''
********************************************************************************
                        Employee Data Entry Application                         
********************************************************************************
'''
print(__doc__)

# You will also provide a menu interface for the user. This code should be
# outside the class definition and construct objects and call methods from the
# class definition as required.

if __name__ == "__main__":

    # Employee class defintion
    class Employee:
        # Employee ID number
        __eid = 1
        # You need to include a constructor.
        def __init__(self, name="", hours=0, rate=0):
            self.__eid = Employee.__eid
            Employee.__eid += 1
            self.name = name
            self.hours = hours
            self.rate = rate
            self.set_hours(hours)
            self.set_rate(rate)
            
        # You need to write getters and setters for the name, hours, and rate
        # instance variables (6 methods total). The setters for hours and rate
        # should validate the data (make sure it is greater than 0).
        def set_name(self, name):
            self.name = name
        def set_hours(self, hours):
            if hours > 0:
                self.hours = hours
        def set_rate(self, rate):
            if rate > 0:
                self.rate = rate
        def get_name(self):
            return self.name
        def get_hours(self):
            return self.hours
        def get_rate(self):
            return self.rate
        ## ADDED for EID
        def get_eid(self):
            return self.__eid

        # The get_input and calc_pay functions should become methods of the class.
        # They will need a few modifications.
        def get_input(self):
            # The get_input function should set the appropriate instance
            # variables (after prompting the user) instead of returning them.
            '''Prompts for name, hours, and rate. Returns the name (str), hours
            worked (float), and hourly rate (float) for one employee.'''
            # Prompt the user for employee's name
            name = str(input("Enter employee name: "))
            self.set_name(name)
            # Prompt the user for hours worked
            hours = float(input("Enter hours worked: "))
            self.set_hours(hours)
            # Prompt the user for hourly rate
            rate = float(input("Enter hourly rate: "))
            self.set_rate(rate)

        def calc_pay(self):
            # The calc_pay will no longer need arguments because hours and
            # hourly rate are now instance variables.
            '''Returns the amount the employee gets paid for the week. If the
            employee works over 40 hours, they should receive 1.5 times their
            hourly rate for all hours worked over 40.'''
            # determine base pay
            pay = self.hours * self.rate
            # determine if overtime was worked
            if self.hours > 40:
                # determine overtime hours
                pay = (1.5 * self.rate) * self.hours            
            return pay

    '''Initial Employee entry'''
    # The menu will initially allow the user to enter an employee or quit the
    # application.
    print("1: Enter an employee\nq: Quit the application")
    employee = Employee("employee", 1, 1)
    employee_info = {"EID": 0, "Name": employee.get_name(), "Hours": 0,
                     "Rate": 0, "Pay": 0}
##    control = input()
##    print()
##
##    if control == "1":
##        employee.get_input()
##    elif control == "q":
##        print("quitting...\n")
##    else:
##        print("invalid input.\n")
    
    employee.get_input()
    employee_info["EID"] = employee.get_eid()
    employee_info["Name"] = employee.get_name()
    employee_info["Hours"] += employee.get_hours()
    employee_info["Rate"] += employee.get_rate()
    employee_info["Pay"] += employee.calc_pay()
    print(employee_info)

    

    # Once the user has entered an employee, the option to print all employees
    # should be added to the menu.

    # if input = 1, prompt is now added 2: Print employee list

    # When the user quits the application, print the total and average pay for
    # all employees entered during that session.
    

    # If no employees were entered, print something stating no employees were
    # entered.
