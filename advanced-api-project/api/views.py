from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
# Required for filter backend setup (used by DjangoFilterBackend)
from django_filters import rest_framework as filters # type: ignore
from rest_framework.filters import SearchFilter



# List all books

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.DjangoFilterBackend,     # Enables filtering
        filters.OrderingFilter,          # Enables ordering
        SearchFilter                     # Enables search
    ]

    # Filter, Search, and Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access


# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only


# BookListView:
# Returns a list of all books.
# Accessible by anyone (no authentication required).

# BookDetailView:
# Returns details of a single book using its ID.
# Public endpoint.

# BookCreateView:
# Allows authenticated users to create new Book instances.
# Validates input data via BookSerializer.

# BookUpdateView:
# Authenticated users can update an existing book by ID.

# BookDeleteView:
# Authenticated users can delete a book by ID.

filter_backends = [filters.DjangoFilterBackend, filters.OrderingFilter, SearchFilter]
filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
