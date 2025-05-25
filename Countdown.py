class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # Return the iterator object (usually self)
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop when countdown is below 0
        else:
            value = self.current
            self.current -= 1
            return value

# Create a Countdown object
cd = Countdown(5)

# Use in a for-loop
for number in cd:
    print(number)
