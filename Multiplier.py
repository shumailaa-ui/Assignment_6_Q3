class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an instance of Multiplier
double = Multiplier(2)

# Test if the object is callable
print("Is 'double' callable?", callable(double))

# Use the object like a function
result = double(10)
print("double(10) =", result)
