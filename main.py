import book
import library


# Create Book instances.
first_book = book.Book("1984", "George Orwell", "9780451524935", 3)
second_book = book.Book("The Odyssey", "Homer", "9780140268867", 3)
third_book = book.Book("Crime and Punishment", "Fyodor Dostoevsky", "9780486454115", 2)

#Initialize Library with books.
book_list = library.Library([first_book, second_book, third_book])

def menu():
    print("""
******* Library Management System ********
1. Add a new book.
2. Remove a book.
3. List all books.
4. Search books by title.
5. Search books by author.
6. Borrow a book.
7. Exit.
    """)

def start():
    while True:
        menu()
        try:
            user_input = int(input("Please choose a number: "))
        except ValueError :
            print("Invalid input. Please enter a number between 1 and 7.")
            continue
        if user_input == 1 :
            title = input("Enter book title:")
            auther = input("Enter book author:")
            isbn = input("Enter book ISBN: ")
            quantity = int(input("Enter book quantity:"))
            book_list.add_book(title,auther,isbn,quantity)

        elif user_input == 2:
            title_to_remove = input("Enter the title to remove: ")
            book_list.remove_book(title_to_remove)

        elif user_input == 3:
           book_list.list_books()

        elif user_input == 4 :
            book_list.list_books()
            book_title = input("Enter the title of the book: ")
            print(book_list.search_by_title(book_title))

        elif user_input == 5:
            book_list.list_books()
            book_auther = input("Enter the auther of the book: ")
            print(book_list.search_by_author(book_auther))

        elif user_input == 6 :
            book_list.list_books()
            book = input("Enter book title to borrow: ")
            print(book_list.borrow_book(book))

        elif user_input == 7:
            print("Thank you for using the Library Management System. Goodbye!")
            break




if __name__ == "__main__":
    start()








