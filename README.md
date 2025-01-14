# Library Management System

This is a Python-based Library Management System that allows users to manage a collection of books. The system provides functionalities for adding, removing, listing, searching, borrowing, and updating the quantity of books. Book information is now stored in a JSON file for persistence.

## Features

1. **Add a Book**
   - Add a new book to the library by specifying the title, author, ISBN, and quantity.

2. **Remove a Book**
   - Remove a specific book from the library collection.

3. **List All Books**
   - Display all books in the library with their details, including title, author, ISBN, and quantity.

4. **Search Books**
   - Search for books by title or author.

5. **Borrow a Book**
   - Borrow a book from the library. The quantity of the book is reduced by one.

6. **Change Quantity**
   - Update the quantity of a specific book in the library.

7. **Persistent Storage**
   - Book information is stored in a JSON file, enabling data persistence across sessions.

## Prerequisites

- Python 3.x

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2.Ensure the `books.json` file is present in the project directory. This file contains the initial book data.

## How to Run

1. Execute the `main.py` file to start the application:
   ```bash
   python main.py
   ```

2. Follow the on-screen menu to interact with the system.

## JSON Integration

The `books.json` file is used to store book data in the following format:

```json
[
  {
    "title": "1984",
    "author": "George Orwell",
    "isbn": "9780451524935",
    "quantity": 3
  },
  {
    "title": "The Odyssey",
    "author": "Homer",
    "isbn": "9780140268867",
    "quantity": 3
  },
  {
    "title": "Crime and Punishment",
    "author": "Fyodor Dostoevsky",
    "isbn": "9780486454115",
    "quantity": 2
  }
]
```

## Example Interaction

1. **List All Books:**
   ```
   1. 1984 by George Orwell (ISBN: 9780451524935) - Quantity: 3
   2. The Odyssey by Homer (ISBN: 9780140268867) - Quantity: 3
   3. Crime and Punishment by Fyodor Dostoevsky (ISBN: 9780486454115) - Quantity: 2
   ```

2. **Add a New Book:**
   ```
   Enter book title: Brave New World
   Enter book author: Aldous Huxley
   Enter book ISBN: 9780060850524
   Enter book quantity: 5
   'Brave New World' added to the Library successfully.
   ```

3. **Change Book Quantity:**
   ```
   Enter the title of the book to update: 1984
   Enter the new quantity: 10
   Quantity for '1984' updated to 10.
   ```




