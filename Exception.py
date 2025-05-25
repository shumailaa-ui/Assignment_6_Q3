# Step 1: Define a custom exception
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Must be 18 or older.")

# Step 2: Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Access granted!")

# Step 3: Use try...except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid number.")
