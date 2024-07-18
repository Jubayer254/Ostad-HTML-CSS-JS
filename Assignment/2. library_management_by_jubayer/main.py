import json
from tabulate import tabulate

books = []
lent_books = []

def load_books():
    global books, lent_books
    try:
        with open('books.json', 'r') as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        books = []

    try:
        with open('lent_books.json', 'r') as file:
            lent_books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        lent_books = []

def save_books():
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

    with open('lent_books.json', 'w') as file:
        json.dump(lent_books, file, indent=4)

def generate_id():
    if books:
        return max(book['id'] for book in books) + 1
    return 1

def generate_lend_id():
    if lent_books:
        return max(lent_book['id'] for lent_book in lent_books) + 1
    return 1

def add_book():
    title = input("Enter Title: ")
    authors = input("Enter Author(s) (separated by commas if multiple): ").split(',')
    ISBN = input("Enter ISBN: ")

    try:
        publishing_year = int(input("Enter Publishing Year: "))
    except ValueError:
        print("The publishing year should be an integer number")
        return
    
    try:
        price = float(input("Enter Price: "))
    except ValueError:
        print("The book price should be a float number")
        return
    
    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("The quantity should be an integer number")
        return

    book = {
        'id': generate_id(),
        'title': title,
        'authors': [author.strip() for author in authors],
        'ISBN': ISBN,
        'publishing_year': publishing_year,
        'price': price,
        'quantity': quantity
    }

    books.append(book)
    save_books()
    print("Book added successfully!\n")

def view_books():
    if not books:
        print("No books available.")
        return

    table_data = []
    for book in books:
        table_data.append([
            book['id'],
            book['title'],
            ', '.join(book['authors']),
            book['ISBN'],
            book['publishing_year'],
            book['price'],
            book['quantity']
        ])

    headers = ["ID", "Title", "Authors", "ISBN", "Publishing Year", "Price", "Quantity"]
    table_str = tabulate(table_data, headers, tablefmt="pretty")
    print(table_str)

def search_books(term):
    if not books:
        print("No books available.")
        return

    table_data = []
    for book in books:
        if term.lower() in book['title'].lower() or term in book['ISBN']:
            table_data.append([
                book['id'],
                book['title'],
                ', '.join(book['authors']),
                book['ISBN'],
                book['publishing_year'],
                book['price'],
                book['quantity']
            ])

    if not table_data:
        print("No books found for the search term.")
    else:
        headers = ["ID", "Title", "Authors", "ISBN", "Publishing Year", "Price", "Quantity"]
        table_str = tabulate(table_data, headers, tablefmt="pretty")
        print(table_str)

def search_books_by_author(author_name):
    if not books:
        print("No books available.")
        return

    table_data = []
    for book in books:
        for author in book['authors']:
            if author_name.lower() in author.lower():
                table_data.append([
                    book['id'],
                    book['title'],
                    ', '.join(book['authors']),
                    book['ISBN'],
                    book['publishing_year'],
                    book['price'],
                    book['quantity']
                ])
                break

    if not table_data:
        print("No books found for the search term.")
    else:
        headers = ["ID", "Title", "Authors", "ISBN", "Publishing Year", "Price", "Quantity"]
        table_str = tabulate(table_data, headers, tablefmt="pretty")
        print(table_str)

def lend_book():
    global books, lent_books
    if not books:
        print("No books available to lend.")
        return

    view_books()
    try:
        book_id = int(input("Enter the ID of the book you want to lend: "))
        found_book = False

        for book in books:
            if book['id'] == book_id:
                found_book = True
                if book['quantity'] > 0:
                    borrower_name = input("Enter borrower's name: ")
                    borrower_contact = input("Enter borrower's contact information: ")
                    book['quantity'] -= 1
                    lent_book = {
                        'id': generate_lend_id(),
                        'title': book['title'],
                        'borrower': {
                            'name': borrower_name,
                            'contact': borrower_contact
                        }
                    }
                    lent_books.append(lent_book)
                    save_books()  # Save both books and lent_books
                    print(f"Book '{book['title']}' lent to {borrower_name} successfully!\n")
                else:
                    print("No books available to lend for this title.")
                break
        
        if not found_book:
            print("Invalid ID. No book lent.")

    except ValueError:
        print("Invalid input. No book lent.")

def view_lent_books():
    if not lent_books:
        print("No books have been lent.")
        return

    table_data = []
    for lent_book in lent_books:
        table_data.append([
            lent_book['id'],
            lent_book['title'],
            lent_book['borrower']['name'],
            lent_book['borrower']['contact']
        ])

    headers = ["ID", "Title", "Borrower Name", "Borrower Contact"]
    table_str = tabulate(table_data, headers, tablefmt="pretty")
    print(table_str)

def return_book():
    global books, lent_books
    if not lent_books:
        print("No books have been lent.")
        return

    view_lent_books()
    try:
        book_id = int(input("Enter the ID of the book you want to return: "))
        found_book = False

        for lent_book in lent_books:
            if lent_book['id'] == book_id:
                found_book = True
                book_to_update = next((book for book in books if book['id'] == book_id), None)
                if book_to_update:
                    book_to_update['quantity'] += 1
                    lent_books.remove(lent_book)
                    save_books()
                    print(f"Book '{lent_book['title']}' returned successfully!\n")
                else:
                    print("Book not found in the database. Unable to return.")
                break
        
        if not found_book:
            print("Book not found in lent books list. Unable to return.")

    except ValueError:
        print("Invalid input. No book returned.")

def remove_book():
    if not books:
        print("No books available.")
        return

    view_books()

    try:
        book_id = int(input("Enter the ID of the book you want to remove: "))
        found_book = False

        for book in books:
            if book['id'] == book_id:
                found_book = True
                confirmation = input(f"Are you sure you want to remove '{book['title']}'? (y/N): ").strip().lower()
                if confirmation == 'y':
                    books.remove(book)
                    save_books()
                    print(f"Book '{book['title']}' removed successfully!\n")
                else:
                    print("Book removal cancelled.")
                break
        
        if not found_book:
            print("Invalid ID. No book removed.")

    except ValueError:
        print("Invalid input. No book removed.")

if __name__=="__main__":  
    load_books()

    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books by Title or ISBN")
        print("4. Search Books by Author")
        print("5. Lend a Book")
        print("6. View Lent Books")
        print("7. Return a Book")
        print("8. Remove a Book")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_term = input("Enter title or ISBN to search: ")
            search_books(search_term)
        elif choice == '4':
            author_name = input("Enter author name to search: ")
            search_books_by_author(author_name)
        elif choice == '5':
            lend_book()
        elif choice == '6':
            view_lent_books()
        elif choice == '7':
            return_book()
        elif choice == '8':
            remove_book()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")
