from django.db import models
from django.db import models

class Author(models.Model):
    """
    Model representing an author.
    Fields:
        name (str): The author's name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    Fields:
        title (str): Title of the book.
        publication_year (int): Year the book was published.
        author (ForeignKey): Link to the related Author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

