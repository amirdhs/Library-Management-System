import book
from book import first_book, second_book, third_book


class Library:
    def __init__(self,books):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"{book} added to the Library successfully.")

    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError("This book doesnt exist in Library.")

    def list_books(self):
        for book in self.books:
            print("List of Books:")
            print(book)

    def search_by_title(self,title):
        for book in self.books:
            if title in book:
                return book
            else:
                return "This book doesnt exist in Library."

book_list = [first_book,second_book,third_book]


