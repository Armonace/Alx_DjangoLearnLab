1. Overview

This authentication system uses Django’s built-in authentication framework to provide:

User Registration (username, email, password)

Login & Logout

Profile Management (view & update details)

It is secure, CSRF-protected, and follows Django’s recommended password hashing system (PBKDF2).

2. File Structure
blog/
│
├── forms.py               # Custom user registration form
├── views.py               # Views for registration, profile, login, logout
├── urls.py                 # Authentication routes
├── templates/
│   └── blog/
│       ├── login.html      # Login template
│       ├── logout.html     # Logout confirmation
│       ├── register.html   # Registration form
│       └── profile.html    # Profile view/edit page

3. Setup Instructions
Step 1 — Install Django
pip install django

Step 2 — Enable Required Apps in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Your app
]

Step 3 — Configure Authentication Redirects

Add to settings.py:

LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'

Step 4 — Create URLs in blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

Step 5 — Run Migrations
python manage.py migrate

4. Features
Login

Uses Django’s LoginView

Requires username and password

Redirects to profile page after login

Logout

Uses Django’s LogoutView

Redirects to login page after logout

Registration

Custom form (UserRegisterForm) extends Django’s UserCreationForm

Adds email field

Redirects to login page after successful registration

Profile Management

Authenticated users can view & edit their profile

Supports updating username & email

Can be extended to support profile picture, bio, etc.

5. Security

CSRF Protection: All forms use {% csrf_token %}

Password Hashing: Uses Django’s PBKDF2 algorithm

Access Control: Profile view requires login (@login_required)

Session Authentication: Secure server-side sessions

6. Testing the Authentication System
Manual Testing

Register a new account

Log in using the new account

Access /profile/ to confirm login works

Log out and verify /profile/ is inaccessible

Automated Testing (blog/tests/test_auth.py)
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login(self):
        user = User.objects.create_user(username='testuser', password='Testpass123!')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'Testpass123!'
        })
        self.assertEqual(response.status_code, 302)

    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # redirect to login

7. Common Issues & Fixes
Issue	Cause	Solution
Login keeps redirecting to login page	Missing LOGIN_REDIRECT_URL	Add LOGIN_REDIRECT_URL = 'profile' in settings.py
Static files not loading	{% load static %} missing in HTML	Add {% load static %} to templates
Registration fails	Weak or mismatched passwords	Ensure both match & meet Django password rules
8. User Guide
Register

Go to /register/

Fill in username, email, password, and confirmation

Click Register

Login

Go to /login/

Enter username and password

Click Login

Edit Profile

Go to /profile/ while logged in

Update username or email

Save changes

Logout

Click Logout

You’ll be redirected to login page