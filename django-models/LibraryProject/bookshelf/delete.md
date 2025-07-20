## how to delete
from bookshelf.models import Book

# Retrieve the book you want to delete
### command 
'''python
book = Book.objects.get(title="1984")

# Delete the book
'''python
book.delete()


 ## output
 '''bash
> (1, {'bookshelf.BOOK': 1})
