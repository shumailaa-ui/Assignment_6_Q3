# Define the class Car
class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand  # public variable

    # Public method
    def start(self):
        print(f"{self.brand} car has started.")

# Instantiate the class
my_car = Car("Toyota")

# Access the public variable
print("Brand of the car:", my_car.brand)

# Call the public method
my_car.start()
