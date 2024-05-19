# You're working on a program to manage a library's book inventory.
# Write a Python function to remove a book from the inventory given its title?

def remove_book(books, title):
    for i, book in enumerate(books):
        if book["title"] == title:
            del books[i]
            print(f"'{title}' has been removed from the inventory.")
            return
    print(f"'{title}' not found in the inventory.")

if __name__ == '__main__':
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "Pride and Prejudice", "author": "Jane Austen"},
    ]

    title_to_remove = input("Enter the title of the book you wnat to remove: ")
    remove_book(books, title_to_remove)
    print(books)
