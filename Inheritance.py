# Base class A
class A:
    def show(self):
        print("A's show() method")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("B's show() method")

# Class C inherits from A and overrides show()
class C(A):
    def show(self):
        print("C's show() method")

# Class D inherits from both B and C
class D(B, C):
    pass

# Create object of class D
d = D()

# Call the show method
d.show()

# Print the MRO
print("Method Resolution Order (MRO):")
print(D.__mro__)
