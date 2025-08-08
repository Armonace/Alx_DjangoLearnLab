from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='John Doe')
        self.book = Book.objects.create(
            title='Test Book',
            description='Test Description',
            author=self.author
        )

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_retrieve_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "description": "A new book description",
            "author": self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "description": "Updated description",
            "author": self.author.id
        }
        response = self.client.put(f'/api/books/{self.book.id}/update/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
