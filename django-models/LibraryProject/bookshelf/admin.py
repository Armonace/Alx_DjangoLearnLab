from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in admin list
    list_filter = ('author', 'publication_year')            # Filters in the sidebar
    search_fields = ('title', 'author')                     # Search bar fields


admin.site.register(Book, BookAdmin)
