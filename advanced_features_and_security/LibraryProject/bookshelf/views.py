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
