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
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
