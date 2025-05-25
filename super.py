# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Create an object of Teacher
teacher1 = Teacher("Shumaila Usmani", "Python Programming")

# Display the teacher's information
teacher1.display_info()
