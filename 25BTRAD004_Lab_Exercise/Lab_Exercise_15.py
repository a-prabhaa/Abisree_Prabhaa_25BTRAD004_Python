class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.available = True
    def display_details(self):
        print("Book Title:", self.title)
        print("Book ID:", self.item_id)
        print("Availability:", "Available" if self.available else "Issued")
# Child Class (Inheritance)
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
# Issue Book
    def issue_book(self):
        if self.available:
            self.available = False
            print(self.title, "has been issued successfully.")
        else:
            print(self.title, "is already issued. Book not available.")
    # Return Book
    def return_book(self):
        if not self.available:
            self.available = True
            print(self.title, "has been returned successfully.")
        else:
            print(self.title, "was not issued. Cannot return.")
    # Display Book Details
def display_details(self):
        super().display_details()
        print("Author:", self.author)
# Creating Book Objects
book1 = Book("Python Programming", 101, "John Smith")
book2 = Book("Data Structures", 102, "Mark Allen")
# Display Initial Details
print("--- Initial Book Details ---")
book1.display_details()
print()
book2.display_details()
# Issuing Books
print("\n--- Issuing Books ---")
book1.issue_book()
book1.issue_book()  # Testing unavailable book
# Returning Books
print("\n--- Returning Books ---")
book1.return_book()
book1.return_book()  # Testing invalid return
# Checking Availability
print("\n--- Final Book Status ---")
book1.display_details()
print()
book2.display_details()
