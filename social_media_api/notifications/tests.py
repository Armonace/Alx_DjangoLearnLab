from django.test import TestCase

# posts/tests.py
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Like

User = get_user_model()

class LikeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass1234")
        self.post = Post.objects.create(author=self.user, content="Hello world")
        self.client.login(username="test", password="pass1234")

    def test_like_post(self):
        response = self.client.post(f"/posts/{self.post.id}/like/")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.count(), 1)

    def test_unlike_post(self):
        self.client.post(f"/posts/{self.post.id}/like/")
        response = self.client.post(f"/posts/{self.post.id}/unlike/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Like.objects.count(), 0)
