## This is how to create a book instance

### command
'''python
>>> from bookshelf.models import BOOK
>>> BOOK.objects.create(title="valkyrie", author="George Orwell", publication_year=2025)
'''



### output
'''bash
<BOOK: BOOK object (1)>
