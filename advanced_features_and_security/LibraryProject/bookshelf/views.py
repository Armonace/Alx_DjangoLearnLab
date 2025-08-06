from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the home page!")

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Article

@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'bookshelf/article_list.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request):
    # logic to create article
    ...

@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    # logic to edit article
    ...

@permission_required('bookshelf.can_delete', raise_exception=True)
def article_delete(request, pk):
    # logic to delete article
    ...
from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.shortcuts import render, redirect
from .forms import BookForm  # You must have a BookForm defined

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Or any view name you have
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})



def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})
