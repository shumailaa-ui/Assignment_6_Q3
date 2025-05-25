class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Call static method directly using class name
result = MathUtils.add(10, 20)
print("The sum is:", result)
