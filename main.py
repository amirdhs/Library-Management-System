import json

import book
import library
import json

# Create Book instances.
# first_book = book.Book("1984", "George Orwell", "9780451524935", 3)
# second_book = book.Book("The Odyssey", "Homer", "9780140268867", 3)
# third_book = book.Book("Crime and Punishment", "Fyodor Dostoevsky", "9780486454115", 2)

# json file
with open("books.json", "r") as file:
    data = json.load(file)

book_list = []
for book_element in data:
    book_object = book.Book(book_element["title"],book_element["author"],book_element["isbn"],book_element["quantity"])
    book_list.append(book_object)

#Initialize Library with books.
book_list = library.Library(book_list)


def menu():
    print("""
******* Library Management System ********
1. Add a new book.
2. Remove a book.
3. List all books.
4. Search books by title.
5. Search books by author.
6. Borrow a book.
7. Change Quantity
8. Exit.
    """)

def start():
    while True:
        menu()
        try:
            user_input = int(input("Please choose a number: "))
        except ValueError :
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if user_input == 1:
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            try:
                quantity = int(input("Enter book quantity: "))
                book_list.add_book(title, author, isbn, quantity)
                print(f"Book '{title}' added successfully!")
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")

        elif user_input == 2:
            title_to_remove = input("Enter the title to remove: ").strip()
            try:
                book_list.remove_book(title_to_remove)
                print(f"Book '{title_to_remove}' removed successfully!")
            except ValueError as e:
                print(e)

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
            book = input("Enter book title to borrow: ").strip()
            print(book_list.borrow_book(book))

        elif user_input == 7:
            new_quantity = int(input("Enter new Quantity: "))
            title = input("enter the title :")
            temp_book = book_list.return_book_by_title(title)
            temp_book.update_quantity(new_quantity)


        elif user_input == 8:
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    start()








