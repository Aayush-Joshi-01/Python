def get_library_summary(books):
    total_books = len(books)
    total_rating = sum(book['rating'] for book in books)
    average_rating = total_rating / total_books
    highest_rated_book = max(books, key=lambda x: x['rating'])
    return {
        'total_books': total_books,
        'average_rating': average_rating,
        'highest_rated_book': highest_rated_book,
    }


def search_books_by_genre(books, genre):
    return [book for book in books if book['genre'] == genre]


if __name__ == '__main__':
    books = [
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'rating': 4.5, 'genre': 'Fiction'},
        {'title': '1984', 'author': 'George Orwell', 'rating': 4.2, 'genre': 'Science Fiction'},
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'rating': 4.3, 'genre': 'Fiction'},
        {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'rating': 4.0, 'genre': 'Fiction'},
        {'title': 'Brave New World', 'author': 'Aldous Huxley', 'rating': 4.1, 'genre': 'Science Fiction'},
    ]
    library_summary = get_library_summary(books)
    print(f"Total number of books: {library_summary['total_books']}")
    print(f"Average rating per book: {library_summary['average_rating']:.2f}")
    print(
        f"Book with the highest rating: {library_summary['highest_rated_book']['title']} by {library_summary['highest_rated_book']['author']} with rating {library_summary['highest_rated_book']['rating']:.2f}")
    fiction_books = search_books_by_genre(books, 'Fiction')
    print(f"Fiction books: {[book['title'] for book in fiction_books]}")
