class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private

    def show_info(self):
        print("Inside class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

# Create object of Employee
emp = Employee("Ali", 50000, "123-45-6789")

# Access variables
print("Outside class:")
print("Public (name):", emp.name)         # ✅ will work
print("Protected (_salary):", emp._salary) # ✅ works, but convention says use it carefully
# print("Private (__ssn):", emp.__ssn)     # ❌ will cause error

# Instead, access private variable using name mangling:
print("Private (__ssn) using name mangling:", emp._Employee__ssn)

# Call method to show info from inside class
emp.show_info()
