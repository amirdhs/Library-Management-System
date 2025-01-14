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

    def remove_book(self, title_to_remove):
        for book in self.books:
            if title_to_remove.lower() in book.title.lower():
                self.books.remove(book)
                print(f"'{book.title}' removed from the Library successfully.")
                return
        raise ValueError(f"'{title_to_remove}' doesn't exist in the Library.")

    def list_books(self):
        if not self.books:
            print("No books in the Library.")
            return
        print("List of Books:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.show_info()}")

    def search_by_title(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book.show_info()
        return "This book doesn't exist in the Library."

    def return_book_by_title(self,title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return "This book doesn't exist in the Library."

    def search_by_author(self,author):
        for book in self.books:
            if author.lower() in book.author.lower():
                return book.show_info()
        return "This book doesn't exist in the Library."

    def borrow_book(self,title):
        for book in self.books:
            if title.lower() in book.title.lower():
                book.quantity -= 1
                return f"You have successfully borrowed: {book.title}"
        return f"{title} doesn't exist in the Library."




