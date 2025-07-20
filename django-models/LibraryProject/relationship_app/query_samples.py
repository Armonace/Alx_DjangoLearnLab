import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library

# Query 1: All books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"\nAuthor '{author_name}' not found.")

# Query 2: All books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name} Library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"\nLibrarian for {library_name} Library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
    except:
        print(f"\nNo librarian assigned to {library_name} Library.")

# Sample queries
if __name__ == "__main__":
    get_books_by_author("George Orwell")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
