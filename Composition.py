# Engine class
class Engine:
    def start(self):
        print("Engine started.")

# Car class that uses Engine via composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car HAS an Engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Accessing Engine's method through Car

# Create an Engine object
my_engine = Engine()

# Pass the Engine object to the Car
my_car = Car(my_engine)

# Start the car (which uses the Engine)
my_car.start_car()
