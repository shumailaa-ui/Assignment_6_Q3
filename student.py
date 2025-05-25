class Student:
    # Constructor to initialize name and marks
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to display student details
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Create an object of Student class
student1 = Student("Ali", 88)

# Call the display method
student1.display()
