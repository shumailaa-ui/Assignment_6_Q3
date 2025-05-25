class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")

# Creating an object of Logger class
log = Logger()

# Optional: Manually delete the object (or wait for program to end)
del log
