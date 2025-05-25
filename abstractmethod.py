from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  # Abstract method with no implementation

# Derived class
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create a Rectangle object
rect = Rectangle(5, 3)

# Print the area of the rectangle
print("Area of Rectangle:", rect.area())
