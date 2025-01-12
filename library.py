import book

class Library:
    def __init__(self, books=None):
        if books:
            self.books = books
        else:
            self.books = []

    def add_book(self, title, author, isbn, quantity):
        new_book = book.Book(title, author, isbn, quantity)
        self.books.append(new_book)
        print(f"'{title}' added to the Library successfully.")

    def remove_book(self, book_to_remove):
        if book_to_remove in self.books:
            self.books.remove(book_to_remove)
            print(f"'{book_to_remove.title}' removed from the Library successfully.")
        else:
            raise ValueError("This book doesn't exist in the Library.")

    def list_books(self):
        print("List of Books:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.show_info()}")

    def search_by_title(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book.show_info()
        return "This book doesn't exist in the Library."

    def search_by_author(self,author):
        for book in self.books:
            if author.lower() in book.author.lower():
                return book.show_info()
        return "This book doesn't exist in the Library."

    # def borrow_book(self,title):
    #     for book in self.books:
    #         if title.lower() in self.books:
    #             book.quantity -= 1
    #             return f"You borrow this book {book}"
    #     return "This book doesn't exist in the Library."



# Create Book instances.
first_book = book.Book("1984", "George Orwell", "9780451524935", 3)
second_book = book.Book("The Odyssey", "Homer", "9780140268867", 3)
third_book = book.Book("Crime and Punishment", "Fyodor Dostoevsky", "9780486454115", 2)

# Initialize Library with books.
book_list = Library([first_book, second_book, third_book])

# Add a new book.
book_list.add_book("2023", "Amir", "234564", 4)

# List all books.
book_list.list_books()

# Search for a book by title.
print(book_list.search_by_title("1984"))

# Search fot a book by auther
print(book_list.search_by_author("Homer"))

# Borrow a book
print(book_list.borrow_book("1984"))