# Library Management System

This is a Python-based Library Management System that allows users to manage a collection of books. It supports adding, removing, searching, listing, and borrowing books from the library.

## Features

- **Add a Book**: Add a new book to the library by specifying its title, author, ISBN, and quantity.
- **Remove a Book**: Remove a book from the library by its title.
- **List All Books**: Display a list of all books currently available in the library.
- **Search by Title**: Find books by their title.
- **Search by Author**: Find books by their author.
- **Borrow a Book**: Borrow a book from the library and decrease its available quantity.

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```

3. Ensure all necessary files are available:
   - `book.py`: Contains the `Book` class for representing individual books.
   - `library.py`: Contains the `Library` class for managing the collection of books.
   - `main.py`: The entry point for running the program.

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Follow the on-screen menu to interact with the Library Management System.

### Menu Options

1. **Add a Book**
   - Provide the book's title, author, ISBN, and quantity.
   - Example: `"1984", "George Orwell", "9780451524935", 5`

2. **Remove a Book**
   - Enter the title of the book you want to remove.

3. **List All Books**
   - Displays all books with their details, including title, author, ISBN, and available quantity.

4. **Search by Title**
   - Enter the title (or a part of it) to find matching books.

5. **Search by Author**
   - Enter the author's name (or a part of it) to find matching books.

6. **Borrow a Book**
   - Enter the title of the book you want to borrow. If available, the book's quantity will decrease by 1.

7. **Exit**
   - Quit the program.

## Example Output

```plaintext
******* Library Management System ********
1. Add a new book.
2. Remove a book.
3. List all books.
4. Search books by title.
5. Search books by author.
6. Borrow a book.
7. Exit.
Please choose a number: 3

List of Books:
1. 1984, Author: George Orwell, ISBN: 9780451524935, Quantity: 3
2. The Odyssey, Author: Homer, ISBN: 9780140268867, Quantity: 3
3. Crime and Punishment, Author: Fyodor Dostoevsky, ISBN: 9780486454115, Quantity: 2
```
