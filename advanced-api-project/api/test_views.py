from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITests(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            description="A sample description",
            published_date="2025-01-01"
        )

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Jane Doe",
            "description": "Another description",
            "published_date": "2025-02-01"
        }
        response = self.client.post('/api/books/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": "John Doe",
            "description": "Updated description",
            "published_date": "2025-01-01"
        }
        response = self.client.put(f'/api/books/{self.book.id}/update/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

