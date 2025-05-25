class Counter:
    # Class variable to keep count
    object_count = 0

    def __init__(self):
        # Increase count each time an object is created
        Counter.object_count += 1

    # Class method to display the count
    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.object_count}")

# Create some objects
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Show total count using class method
Counter.show_count()
