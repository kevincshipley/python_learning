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
                pay += (.5 * self.rate) * self.hours            
            return pay

###########################################################################
    
    # The menu will initially allow the user to enter an employee or quit the
    # application.
    print("1: Enter an employee\nq: Quit the application")
    employee = Employee()
    e_name = []
    e_hours = []
    e_rate = []
    e_pay = []
    control = input()
    print()

    ## START OF LOOP ##
    while control != "q":
        # 1 will prompt for employee information to be entered
        if control == "1":
            employee.get_input()
            e_name.append(employee.get_name())
            e_hours.append(employee.get_hours())
            e_rate.append(employee.get_rate())
            e_pay.append(employee.calc_pay())
            print()
        elif control == "q":
            break
        
        ## END OF LOOP ##
        print("1: Enter an employee\n"
              "2: Print employee list\n"
              "q: Quit the application\n")
        control = input()
        print()
        # Once the user has entered an employee, the option to print all
        # employees should be added to the menu.
        if control == "2":
            i = 0
            for e in e_name:
                print("Name:\t\t{}".format(e_name[i]))
                print("Hours Worked:\t{:,.2f}".format(e_hours[i]))
                print("Hourly Rate:\t${:,.2f}".format(e_rate[i]))
                print()
                i += 1
            continue
        if control == "1": continue
        if control == "q":
            print()
            break

    # When the user quits the application, print the total and average pay for
    # all employees entered during that session.
  
    # If no employees were entered, print something stating no employees were
    # entered.

    print("*" * 80)
    print()
    print("*" * 80)
    print()

    if len(e_name) > 0:
        i = 0
        total_pay = 0
        for i in e_pay:
            total_pay += i
            i += 1
        print("The total amount to be paid is ${:,.2f}".format(total_pay))
        print("The average employee is paid ${:,.2f}".format(total_pay/
                                                             len(e_pay)))

    else:
        print("No employees were entered.")
