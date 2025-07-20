# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)  # ✅ This line is required
print("Books by George Orwell:")
for book in books_by_author:
    print(book.title)

# List all books in a specific library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a specific library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian of {library.name}: {librarian.name}")
