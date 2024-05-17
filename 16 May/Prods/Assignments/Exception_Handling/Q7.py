class BookNotAvailableException(Exception):
    pass


class BookNotBorrowedException(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, title, quantity=1):
        if title in self.books:
            self.books.title += quantity
        else:
            self.books[title] = quantity

    def borrow_book(self, title):
        if title not in self.books or self.books[title] == 0:
            raise BookNotAvailableException(f"The book '{title}' is not available.")
        self.books[title] -= 1
        if title in self.borrowed_books:
            self.borrowed_books[title] += 1
        else:
            self.borrowed_books[title] = 1

    def return_book(self, title):
        if title not in self.borrowed_books or self.borrowed_books[title] == 0:
            raise BookNotBorrowedException(f"The book '{title}' has not been borrowed.")
        self.borrowed_books[title] -= 1
        self.books[title] += 1

    def list_available_books(self):
        return {title: qty for title, qty in self.books.items() if qty > 0}

    def list_borrowed_books(self):
        return {title: qty for title, qty in self.borrowed_books.items() if qty > 0}


def main():
    library = Library()

    # Adding some books to the library
    library.add_book("1984", 3)
    library.add_book("To Kill a Mockingbird", 2)
    library.add_book("The Great Gatsby", 1)

    while True:
        print("\nLibrary Management System:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. Check Available Books")
        print("4. Check Borrowed Books")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            title = input("Enter the title of the book to borrow: ")
            try:
                library.borrow_book(title)
                print(f"Successfully borrowed '{title}'.")
            except BookNotAvailableException as e:
                print(e)
        elif choice == '2':
            title = input("Enter the title of the book to return: ")
            try:
                library.return_book(title)
                print(f"Successfully returned '{title}'.")
            except BookNotBorrowedException as e:
                print(e)
        elif choice == '3':
            available_books = library.list_available_books()
            if available_books:
                print("Available Books:")
                for title, qty in available_books.items():
                    print(f"{title}: {qty} copy/copies")
            else:
                print("No books available.")
        elif choice == '4':
            borrowed_books = library.list_borrowed_books()
            if borrowed_books:
                print("Borrowed Books:")
                for title, qty in borrowed_books.items():
                    print(f"{title}: {qty} copy/copies")
            else:
                print("No books borrowed.")
        elif choice == '5':
            print("Exiting the library management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
