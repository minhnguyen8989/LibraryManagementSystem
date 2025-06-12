"""
Title:       Critical Thinking Assignment #5
Author:      Minh Nguyen
Created:     2025-06-11
Last Edited: 2025-06-11
Description: This program is a comprehensive library management system that allows users to efficiently manage book inventories and borrowing activities.
                Users can add new books by providing the title, author, and number of copies, with input validation to ensure data integrity.
                The system tracks available and borrowed books separately, allowing users to borrow books if copies are available and return them to update the inventory accordingly.
                A menu-driven interface guides users through adding books, borrowing, returning, displaying the current inventory, and exiting the program.
User Input:
    - Add book with (title, author, number of copies)
    - Borrow book with (title)
    - Return book with (title)
    - View inventory display
Program Output:
    - Confirmation of book addition
    - List of available books for borrowing
    - List of available books for returning
    - Display of current library inventory
"""


def main_menu():
    library = []
    borrowed_book = []
    while True:
        print("\nLibrary Management System")
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_new_book(library)
        elif choice == '2':
            borrow_book(library, borrowed_book)
        elif choice == '3':
            return_book(library, borrowed_book)
        elif choice == '4':
            display_inventory(library)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def add_new_book(library):
    print("\nAdd New Book")

    # Input and validation for title
    while True:
        title = input("Enter book title: ").strip()
        if not title:
            print("Title cannot be empty. Please enter a valid title.")
        else:
            break

    # Input and validation for author
    while True:
        author = input("Enter author name: ").strip()
        if not author:
            print("Author cannot be empty. Please enter a valid author name.")
        else:
            break

    # Input and validation for number of copies
    while True:
        copies = input("Enter number of copies: ").strip()
        if not copies.isdigit():
            print("Number of copies must be a positive integer.")
        else:
            copies = int(copies)
            if copies <= 0:
                print("Number of copies must be greater than zero.")
            else:
                break

    # Check if book already exists
    for book in library:
        if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
            # If exists, increase copies
            book['copies'] += copies
            print(f"Updated existing book: '{title}' by {author}. Total copies now: {book['copies']}")
            return

    # If not exists, add new book
    library.append({'title': title, 'author': author, 'copies': copies})
    print(f"Book '{title}' by {author} added with {copies} copies.")


def borrow_book(library, borrowed_book):
    print("\nCurrent Available Books:")

    print(f"{'Title':<30} {'Author':<20} {'Copies':<6}")
    print("-" * 60)
    for book in library:
        print(f"{book['title']:<30} {book['author']:<20} {book['copies']:<6}")

    if not library:
        print("The library is empty. Please add books.")
        return

    title = input("Enter the book title to borrow: ").strip()
    if not title:
        print("Book title cannot be empty.")
        return

    # Search for the book
    for book in library:
        if book['title'].lower() == title.lower():
            if book['copies'] > 0:
                book['copies'] -= 1
                for b in borrowed_book:
                    if b['title'].lower() == book['title'].lower() and b['author'].lower() == book['author'].lower():
                        b['copies'] += 1
                        break
                else:
                    borrowed_book.append({'title': book['title'], 'author': book['author'], 'copies': 1})
                print(f"You have borrowed '{book['title']}'. Copies left: {book['copies']}")
                return
            else:
                print(f"'{book['title']}' is currently out of stock.")
                return
    print(f"Book '{title}' not found in the library.")


def return_book(library, borrowed_book):
    print("\nCurrent Borrowed Books:")

    print(f"{'Title':<30} {'Author':<20} {'Copies':<6}")
    print("-" * 60)
    for book in borrowed_book:
        print(f"{book['title']:<30} {book['author']:<20} {book['copies']:<6}")

    if not borrowed_book:
        print("No books have been borrowed. Nothing to return.")
        return

    title = input("Enter the book title to return: ").strip()
    if not title:
        print("Book title cannot be empty.")
        return

    # Search for the borrowed book
    for i, book in enumerate(borrowed_book):
        if book['title'].lower() == title.lower():
            # Increase the copy count in the library
            for lib_book in library:
                if lib_book['title'].lower() == title.lower():
                    lib_book['copies'] += 1
                    break
            else:
                # This should not happen, but handle just in case
                library.append({'title': book['title'], 'author': book['author'], 'copies': 1})

            # Remove the book from borrowed list
            if book['copies'] > 1:
                book['copies'] -= 1
            else:
                borrowed_book.pop(i)
            print(f"Thank you for returning '{book['title']}'. It has been added back to the library.")
            return

    print(f"Book '{title}' is not found in the borrowed books list.")


def display_inventory(library):
    print("\nLibrary Inventory:")
    if not library:
        print("The library is currently empty. Option 1 to add books")
        return
    print(f"{'Title':<30} {'Author':<20} {'Copies':<6}")
    print("-" * 60)
    for book in library:
        print(f"{book['title']:<30} {book['author']:<20} {book['copies']:<6}")


if __name__ == "__main__":
    main_menu()
