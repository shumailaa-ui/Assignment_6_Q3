class Book:
    total_books = 0  # Class variable shared by all instances

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Create book objects
book1 = Book("Python Basics", "Shumaila Usmani")
book2 = Book("OOP in Python", "Shumaila Usmani")

# Print total number of books
print("Total Books:", Book.get_total_books())
