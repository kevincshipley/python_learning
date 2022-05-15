'''Employee class definition'''

class Employee:

    # Employee ID, a static variable shared by all Employee objects
    __eid = 1
    
    def __init__(self, name="", hours=0, rate=0):
        self.__eid = Employee.__eid
        Employee.__eid += 1
        self.name = name
        self.hours = hours
        self.rate = rate
        self.set_hours(hours)
        self.set_rate(rate)
        
    # setters for name, hours, rate
    def set_name(self, name):
        self.name = name
    def set_hours(self, hours):
        if hours > 0:
            self.hours = hours
    def set_rate(self, rate):
        if rate > 0:
            self.rate = rate
            
    # getters for name, hours, rate
    def get_name(self):
        return self.name
    def get_hours(self):
        return self.hours
    def get_rate(self):
        return self.rate
    ## ADDED for EID
    def get_eid(self):
        return self.__eid

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

##emp_name = input("Employee: ")
##emp_hours = int(input("Hours: "))
##emp_rate = int(input("Rate: "))

##employee = Employee(emp_name, emp_hours, emp_rate)

##print(employee.get_name())
##print(employee.get_hours())
##print(employee.get_rate())

employee = Employee("Monty", 50, 10) # pay is 750

#employee.get_input()

print(employee.get_eid())
print(employee.get_name())
print(employee.get_hours())
print(employee.get_rate())
print(employee.calc_pay())
print()

employee2 = Employee("Slick", 200, 20)

print(employee2.get_eid())
print(employee2.get_name())
print(employee2.get_hours())
print(employee2.get_rate())
print(employee2.calc_pay())
print()

employee3 = Employee("Spin", 10, 10)

print(employee3.get_eid())
print(employee3.get_name())
print(employee3.get_hours())
print(employee3.get_rate())
print(employee3.calc_pay())
print()
