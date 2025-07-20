
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Or wherever you want to go after login
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view to display a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

