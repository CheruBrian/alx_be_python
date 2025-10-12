class Book:
    """Base class representing a generic book."""

    def __init__(self, title, author):
        """Initialize the common book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a readable string representation of a Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """
        Initialize EBook with title, author, and file size.
        Calls the base class constructor for shared attributes.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a readable string representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """
        Initialize PrintBook with title, author, and page count.
        Calls the base class constructor for shared attributes.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a readable string representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class representing a library that holds books (composition)."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book, EBook, or PrintBook instances can be added to the library.")

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
