# bookshelf/forms.py

from django import forms
from .models import Book  # Make sure this points to your Book model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']