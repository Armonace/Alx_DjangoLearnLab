from django.db import models

class Book(models.Model):  # Not BOOK or book, it must be exactly Book
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.CharField()

    def __str__(self):
        return f"{self.title} by {self.author}"
