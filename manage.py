# A simple dictionary to store {Book Title: Availability}
library = {
    "The Hobbit": True,
    "Python Basics": True,
    "Harry Potter": True
}

def show_books():
    print("\n--- Library Inventory ---")
    for book, available in library.items():
        status = "Available" if available else "Borrowed"
        print(f"{book}: {status}")

def borrow_book(title):
    if title in library:
        if library[title]:
            library[title] = False
            print(f"You've borrowed '{title}'.")
        else:
            print("Sorry, that book is already out.")
    else:
        print("We don't have that book.")

def return_book(title):
    if title in library:
        library[title] = True
        print(f"Thank you for returning '{title}'.")
    else:
        print("That book doesn't belong to this library.")

# Quick Test
show_books()
borrow_book("The Hobbit")
show_books()