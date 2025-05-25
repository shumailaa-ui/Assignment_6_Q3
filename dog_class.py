# Define the Dog class
class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance variable
        self.breed = breed    # Instance variable

    # Instance method
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Create an object of Dog
dog1 = Dog("Buddy", "Golden Retriever")

# Call the bark method
dog1.bark()
