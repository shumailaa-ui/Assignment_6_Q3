# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Apply the decorator to the function
@log_function_call
def say_hello():
    print("Hello, Shumaila!")

# Call the decorated function
say_hello()
