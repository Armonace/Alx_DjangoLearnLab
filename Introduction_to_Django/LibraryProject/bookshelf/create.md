## This is how to create a book instance

### command
'''python
>>> from bookshelf.models import BOOK
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
'''



### output
'''bash
<BOOK: BOOK object (1)>
