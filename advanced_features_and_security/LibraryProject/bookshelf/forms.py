# bookshelf/forms.py

from django import forms
from .models import Book  # Make sure this points to your Book model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
