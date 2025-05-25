class Bank:
    # Class variable
    bank_name = "ABC Bank"

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")


# Create instances
cust1 = Bank("Ali")
cust2 = Bank("Sara")

# Show initial details
cust1.show_details()
cust2.show_details()

# Change bank name using class method
Bank.change_bank_name("XYZ Bank")

# Show updated details
cust1.show_details()
cust2.show_details()
