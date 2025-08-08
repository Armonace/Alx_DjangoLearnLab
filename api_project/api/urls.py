from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Optional ListAPIView
    path('', include(router.urls)),  # Routes for full CRUD
     path('api/', include('api.urls')),  # Your app’s API
    path('api-token-auth/', obtain_auth_token),
]


