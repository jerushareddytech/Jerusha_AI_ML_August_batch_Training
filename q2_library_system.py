def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print("Book does not exist.")
    elif book_id in borrowed_books:
        print("Book is already borrowed.")
    else:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed successfully.")
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print("Book was not borrowed.")
def register_member(members, member_id):
    members.add(member_id)
def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")

def main():
    # Dictionary: book_id -> tuple(title, author, year)
    catalog = {}
    # List: keeps track of borrowed book IDs in order
    borrowed_books = []
    # Set: stores unique member IDs
    members = set()
    # Adding 4 books
    add_book(catalog, 101, "Python Basics", "John Smith", 2022)
    add_book(catalog, 102, "Machine Learning", "Andrew Ng", 2021)
    add_book(catalog, 103, "Data Structures", "Robert Lafore", 2020)
    add_book(catalog, 104, "Artificial Intelligence", "Stuart Russell", 2023)
    # Registering 3 members
    register_member(members, 1001)
    register_member(members, 1002)
    register_member(members, 1003)
    # Trying to register the same member again
    register_member(members, 1001)
    print("Registered Members:", members)
    # Borrowing 2 books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)
    print("Borrowed Books:", borrowed_books)
    # Returning 1 book
    return_book(borrowed_books, 101)
    print("Borrowed Books after return:", borrowed_books)
    # Display available books
    show_available(catalog, borrowed_books)
if __name__ == "__main__":
    main()
