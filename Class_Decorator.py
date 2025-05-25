# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add greet method to the class
    return cls

# Apply the decorator to the class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an object of Person
p = Person("Shumaila")

# Call the greet method added by the decorator
print(p.greet())
