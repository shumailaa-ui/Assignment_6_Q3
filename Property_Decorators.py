class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter method
    @property
    def price(self):
        return self._price

    # Setter method
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be negative!")

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create a Product object
product = Product(100)

# Access price using the getter
print("Price:", product.price)

# Update price using the setter
product.price = 150
print("Updated Price:", product.price)

# Attempt to set a negative price
product.price = -50  # Should print an error message

# Delete price using the deleter
del product.price

# Trying to access deleted price will raise an AttributeError
# print(product.price)  # Uncommenting this will raise an error
