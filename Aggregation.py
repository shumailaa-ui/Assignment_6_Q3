# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

# Department class using aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: has a reference to an Employee object

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Accessing Employee's method

# Create an independent Employee object
emp1 = Employee("Shumaila Usmani", 101)

# Create a Department object that uses the existing Employee object
dept1 = Department("Computer Science", emp1)

# Show department and employee details
dept1.show_details()
