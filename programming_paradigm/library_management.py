class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                print(f"Checked out: {title}")
                return
        print(f"Cannot check out: {title} (not available)")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"Cannot return: {title} (not checked out)")

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        for book in available_books:
            print(f"{book.title} by {book.author}")
